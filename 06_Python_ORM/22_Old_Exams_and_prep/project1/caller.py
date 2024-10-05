import os
import django
from django.db.models import Q, Count, F, Case, When, Value, BooleanField

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order, Product


# Create queries within functions

def get_profiles(search_string=None):
    if search_string is None:
        return ""
    query = Q(
        Q(full_name__icontains=search_string) | Q(email__icontains=search_string)
        | Q(phone_number__icontains=search_string)
    )
    profiles = Profile.objects.filter(query).annotate(orders_count=Count('order')).order_by('full_name')

    result = []
    for p in profiles:
        result.append(f"Profile: {p.full_name}, "
                      f"email: {p.email}, phone number: {p.phone_number}, orders: {p.orders_count}")

    return '\n'.join(result)


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()

    if not loyal_profiles.exists():
        return ""

    result = []
    for lp in loyal_profiles:
        result.append(f"Profile: {lp.full_name}, orders: {lp.orders_count}")

    return '\n'.join(result)


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()
    if last_order is None or not last_order.products.exists():
        return ""
    last_products = ', '.join(p.name for p in last_order.products.order_by('name'))
    return f"Last sold products: {last_products}"


def get_top_products():
    products = Product.objects.prefetch_related(
        'order_set'
    ).annotate(
        orders_count=Count('order')
    ).filter(
        orders_count__gt=0
    ).order_by('-orders_count', 'name')[:5]

    if not products.exists():
        return ""

    result = ["Top products:"]
    for p in products:
        result.append(f"{p.name}, sold {p.orders_count} times")

    return '\n'.join(result)


def apply_discounts():
    orders_to_discount = Order.objects.filter(is_completed=False).annotate(products_count=Count('products')
                                                                           ).filter(products_count__gt=2)

    num_of_updated_orders = orders_to_discount.count() if orders_to_discount.exists() else 0

    orders_to_discount.update(total_price=F('total_price') * 0.9)

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():
    oldest_order = Order.objects.prefetch_related('products').filter(is_completed=False).order_by("creation_date").first()

    if oldest_order is None:
        return ""

    oldest_order.products.update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),
            default=F('is_available'),
            output_field=BooleanField()
        )
    )

    oldest_order.is_completed = True
    oldest_order.save()

    return "Order has been completed!"
