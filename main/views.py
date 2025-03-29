from django.shortcuts import redirect, render
from main import models
from .forms import OrderForm
from django.views.generic import TemplateView
from .models import Category, Pet, Staff, Order
from .forms import OrderForm


# Create your views here.
def main(request):
    return render(request, "main/index.html")


class MainView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["staff"] = Staff.objects.all()
        return context


def order(request):
    if request.method == "GET":
        pet_id = request.GET.get('pet')        
        if pet_id:
            pet = Pet.objects.get(id=pet_id)
            form = OrderForm(initial={'animal': pet})
        else:
            form = OrderForm()

        return render(request, "main/order.html", {"form": form})
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")


def pets_list(request):
    category = request.GET.get("category")
    if category:
        pets = Pet.objects.filter(category__slug=category)
    else:
        pets = Pet.objects.all()
    return render(request, "main/pets_list.html", {"pets": pets, 'category': Category.objects.all()})


class Thanks(TemplateView):
    template_name = "main/thanks.html"
