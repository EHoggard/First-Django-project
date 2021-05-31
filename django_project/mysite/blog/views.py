from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        "Name" : "Ebonnee Hoggard",

        "Track" : "Backend(Python)",

        "Message" : "Hi, mentor, you're doing a great job and Thank you"
    }

    d = data.items()
    return HttpResponse(d)

