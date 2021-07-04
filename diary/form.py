from django.forms import ModelForm, fields
from diary.models import Diary
class DiaryForm(ModelForm):
    class Meta:
        model=Diary
        fields=('text',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['text'].widget.attrs.update({
                'class': 'textarea','placeholder':'what\'s on your mind'
        })