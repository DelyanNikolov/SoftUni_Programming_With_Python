from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia_exam_prep.fruits_app.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruitipedia_exam_prep.fruits_app.models import Fruit
from fruitipedia_exam_prep.utils import get_user_obj


# Create your views here.
class CreateFruitPage(CreateView):
    model = Fruit
    form_class = CreateFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class DetailsFruitPage(DetailView):
    model = Fruit
    template_name = 'fruits/details-fruit.html'
    pk_url_kwarg = 'fruitId'


class EditFruitPage(UpdateView):
    model = Fruit
    form_class = EditFruitForm
    pk_url_kwarg = 'fruitId'
    template_name = 'fruits/edit-fruit.html'
    success_url = reverse_lazy('dashboard')


class DeleteFruitPage(DeleteView):
    model = Fruit
    form_class = DeleteFruitForm
    pk_url_kwarg = 'fruitId'
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
