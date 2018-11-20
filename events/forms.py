from django import forms
from .models import Event
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('category', 'name', 'organisers', 'registration_deadline', 'slug', 'image', 'description', 'price',
                  'location', 'start', 'end', 'available',)
        # start = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))


# fields = ('category', 'name', 'organisers', 'registration_deadline', 'slug', 'image', 'description', 'price',
#                   'location', 'start', 'end', 'available',)
