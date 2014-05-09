from django.shortcuts import render
import sys
# Create your views here.
from vendingmachine.models import Bullet
from django.views.generic.base import TemplateView

def start(request):
    print >> sys.stderr, 'Start Fired'
    context = {}
    return render(request, 'vendingmachine/start.html', context)

def license(request):
    print >> sys.stderr, 'License Fired'
    context = {}
    return render(request, 'vendingmachine/license.html', context)