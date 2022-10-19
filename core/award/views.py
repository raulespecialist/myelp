from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views import View
from .models import Business


def business_list(request):
    businesss = Business.objects.all()
    return render(request, 'business/business_list.html', {'businesss':businesss})

def search_business(request):
    """everytime user inputs to search box, this function runs"""
    business = request.GET.get("business")
    businesslist = []
    if business:
        #collect every objects that contains the input text
        business_objects = Business.objects.filter(name__icontains=business).values()
        for business in business_objects:
            businesslist.append(business)
    return JsonResponse({'status':200, 'business':businesslist})