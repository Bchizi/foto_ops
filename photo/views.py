from django.shortcuts import render
#from django.http import HttpResponse
from .models import Image,Location,Category


# Create your views here.
def welcome(request):
    all_images= Image.objects.all()
    category_results = Category.objects.all()  
    location_results = Location.objects.all()
    return render(request,'welcome.html',{'all_images':all_images,'category_results':category_results,'location_results':location_results})


def search_results(request):
    if 'search_pic' in request.GET and request.GET["search_pic"]:
        search_term = request.GET.get("search_pic")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}" 

        return render(request,'search.html',{"message":message ,'all_images':searched_image})

    else:
        message = "you haven't searched for any term yet"
        return render(request,'search.html',{'message':message,})

def get_category(request,category ):
    category_results = Category.objects.all() 
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__category_name = category)
    return render(request,'welcome.html',{"all_images":category_result,'category_results':category_results,'location_results':location_results,})

def get_location(request,location ):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    location_result = Image.objects.filter(image_location__location_name = location)
    return render(request,'welcome.html',{"all_images":location_result,'category_results':category_results,'location_results':location_results})
    



