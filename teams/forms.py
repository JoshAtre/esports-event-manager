from django.forms import ModelForm
from .models import *

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(CreateTeamForm,self).__init__(*args, **kwargs)
            self.fields['color'].required = True
            self.fields['game'].required = True
            self.fields['logo'].required = False


