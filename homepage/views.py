from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class homePageView(TemplateView):
    template_name = "home.html"

# def homePageView(request):
#     return HttpResponse("Hello, World!")
