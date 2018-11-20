from django.shortcuts import render, get_object_or_404
from .models import Category, Accommodation


def accommodation_detail(request, id, slug):
    accommodation = get_object_or_404(Accommodation,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'accommodations/detail.html',
                  {'accommodation': accommodation})

def accommodation_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    accommodations = Accommodation.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        accommodations = accommodations.filter(category=category)

    return render(request,
                  'accommodations/list.html',
                  {'category': category,
                   'categories': categories,
                   'accommodations': accommodations})

