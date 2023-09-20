from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
import json
from main.models import Product



def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_main(request):

    products = Product.objects.all()
    context = {
        'name': 'Roti',
        'description': 'Rasa roti manis yang kita kenal dan sayangi, bread.',
        'price' : 2000,
        'total' : count_item(),
        'products': products,
    }

    return render(request, "main.html", context)


def count_item():
    data = Product.objects.all()
    total = 0
    for product in data:
        total = total + product.price
    return total
