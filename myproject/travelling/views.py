from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    # using ORM to get data
    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})
