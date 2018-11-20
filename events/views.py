from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Event
from .forms import *
from django.utils import timezone


def event_detail(request, id, slug):
    event = get_object_or_404(Event,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'events/detail.html',
                  {'event': event})

def event_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    events = Event.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        events = events.filter(category=category)

    return render(request,
                  'events/list.html',
                  {'category': category,
                   'categories': categories,
                   'events': events})


def event_new(request):
   if request.method == "POST":
       form = EventForm(request.POST)
       if form.is_valid():
           event = form.save(commit=False)
           event.created = timezone.now()
           event.updated = timezone.now()
           event.image = form.cleaned_data['image']
           event.save()
           return redirect('events:event_list')
   else:
       form = EventForm()
   return render(request, 'events/event_new.html', {'form': form})
