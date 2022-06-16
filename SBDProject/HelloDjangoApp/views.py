from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")
'''
def band_listing(request): 
    bands = models.Band.objects.all()
    return render(request, 'bands/band_listing.html', {'bands': bands})

# Create your views here.
'''