from django.forms import ModelForm
from .models import *


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            self.fields['name'].required = True
            self.fields['start_date'].required = True
            self.fields['end_date'].required = True
            self.fields['venues'].required = False
            self.fields['images'].required = False
