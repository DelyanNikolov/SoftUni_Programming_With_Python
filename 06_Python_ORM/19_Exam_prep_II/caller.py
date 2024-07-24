import os

import django
from django.db.models import Q, Count, F, When, Case, Value, BooleanField

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order, Product


# Create queries within functions
def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ""

    query = (Q(full_name__icontains=search_string)
             | Q(email__icontains=search_string)
             | Q(phone_number__icontains=search_string))

    profiles = Profile.objects.filter(query).annotate(orders_count=Count('orders')).order_by('full_name')

    if not profiles.exists():
        return ""

    result = []
    for p in profiles:
        result.append(f"Profile: {p.full_name}, email: {p.email},"
                      f" phone number: {p.phone_number}, orders: {p.orders_count}")
    return '\n'.join(result)


def get_loyal_profiles() -> str:
    loyal_profiles = Profile.objects.get_regular_customers()
    if not loyal_profiles.exists():
        return ""

    return '\n'.join(f"Profile: {p.full_name}, orders: {p.orders_count}" for p in loyal_profiles)


def get_last_sold_products() -> str:
    last_order = Order.objects.prefetch_related('products').last()
    if last_order is None or not last_order.products.exists():
        return ""
    order_products = last_order.products.order_by('name').values_list('name', flat=True)
    return f"Last sold products: {', '.join(order_products)}"


def get_top_products() -> str:
    top_products = Product.objects.annotate(
        orders_count=Count('order')
    ).filter(
        orders_count__gt=0
    ).order_by(
        '-orders_count', 'name'
    )[:5]

    if not top_products.exists():
        return ""

    result = []
    for p in top_products:
        result.append(f"{p.name}, sold {p.orders_count} times")

    return f"Top products:\n{'\n'.join(result)}"


def apply_discounts() -> str:
    orders = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False
    ).update(
        total_price=F('total_price') * 0.9
    )

    return f"Discount applied to {orders} orders."


def complete_order() -> str:
    order = Order.objects.filter(
        is_completed=False
    ).order_by(
        'creation_date'
    ).first()

    if not order:
        return ""

    order.products.update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),
            default=F('is_available'),
            output_field=BooleanField()
        )
    )

    order.is_completed = True
    order.save()

    return "Order has been completed!"

print(get_last_sold_products())
print(get_top_products())
print(apply_discounts())
print(complete_order())