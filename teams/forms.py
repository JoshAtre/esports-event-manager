from django.forms import ModelForm
from .models import *

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(TeamForm,self).__init__(*args, **kwargs)
            self.fields['color'].required = True
            self.fields['game'].required = True
            self.fields['logo'].required = False

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(PlayerForm,self).__init__(*args, **kwargs)
            self.fields['name'].required = True
            self.fields['email'].required = True
            self.fields['discord'].required = True
            self.fields['rank'].required = True
            self.fields['rank_division'].required = True
            self.fields['team'].required = False
            self.fields['profile_photo'].required = False


