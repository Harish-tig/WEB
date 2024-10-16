from django.shortcuts import render
from django.views.decorators.cache import cache_page
import asyncio
from .home import home_function
from .business import business_function
from .innovation import innovation_function
from .culture import culture_function


# Create your views here.

@cache_page(60 * 10)
def scrape_function(request):
    context = asyncio.run(home_function())
    return render(request
                  ,template_name="home.html"
                  ,context=context)

@cache_page(60 * 10)
def inovation(request):
    context = asyncio.run(innovation_function())
    return render(request
                  ,template_name="inovation.html"
                  ,context=context)


@cache_page(60 * 10)
def sports(request):
    return render(request,template_name="sports.html")


@cache_page(60 * 10)
def business(request):
    context = asyncio.run(business_function())
    return render(request
                  , template_name="business.html"
                  , context=context)


@cache_page(60 * 10)
def culture(request):
    context = asyncio.run(culture_function())
    return render(request
           ,template_name='culture.html'
           ,context = context)