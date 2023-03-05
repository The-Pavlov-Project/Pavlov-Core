from django.http import HttpResponse


def home(request):
    return HttpResponse("Pavlov Api Server")
