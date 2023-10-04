from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CompanyForm, ProductsForm
from .models import Company, Products

# Create your views here.


def index(request):
    return render(request, "index.html")


def create_company(request):
    if request.method == "POST":
        cf = CompanyForm(request.POST)
        if cf.is_valid():
            Company.objects.create(**cf.cleaned_data)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'create.html', {'form': CompanyForm()})


def create_product(request):
    if request.method == "POST":
        cf = ProductsForm(request.POST)
        if cf.is_valid():
            Products.objects.create(**cf.cleaned_data)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'create.html', {'form': ProductsForm()})
