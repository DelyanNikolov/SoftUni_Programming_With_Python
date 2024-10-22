from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from WorldOfSpeedApp.cars.forms import CreateCarForm, CarEditForm, CarDeleteForm
from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.profiles.models import Profile


# Create your views here.
def catalogue_page(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()

    context = {
        'cars': cars,
        'profile': profile,
    }

    return render(request, 'cars/catalogue.html', context)


def create_car_page(request):
    form = CreateCarForm(request.POST or None)
    profile = Profile.objects.first()
    if form.is_valid():
        form.instance.owner_id = profile.pk
        form.save()

        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template_name='cars/car-create.html', context=context)


def car_details_page(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car,
    }

    return render(request, template_name='cars/car-details.html', context=context)


class CarEditPage(UpdateView):
    model = Car
    template_name = 'cars/car-edit.html'
    form_class = CarEditForm
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('catalogue')


class CarDeletePage(DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')
    form_class = CarDeleteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Pass the pre-filled form into the template
        context['form'] = CarDeleteForm(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        # When the form is submitted, call the deletion logic
        return self.delete(request, *args, **kwargs)
