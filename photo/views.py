from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to my foto ops')
