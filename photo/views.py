from django.http import HttpResponse

# Create your views here.
def Welcome(request):
    return HttpResponse('welcome to my foto ops')
