from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Business, User, Review
from django.db.models import Avg, Count

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

def business_detail(request, pk=str):
    reviews = Review.objects.select_related('user', 'business').filter(business_id=pk).order_by('-useful', '-stars', '-cool', '-funny')
    average = len(reviews)
    return render(request, 'business/business_detail.html', {'reviews': reviews})

def index(request):
    business = Review.objects.select_related('business').filter().annotate(average_stars = Avg('stars')).order_by('-average_stars')[:10]
    business_r = Review.objects.select_related('business').filter().annotate(business_idr = Count('business_id')).order_by('-business_idr')[:10]
    return render(request, 'business/index.html', {'business': business, 'business_r': business_r})