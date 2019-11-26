from django import forms
from .models import register1
from django.contrib.auth.models import User
class register_form(forms.ModelForm):
    choice_field=(('male','male'),('female','female'),('others','others'))
    gender=forms.TypedChoiceField(choices=choice_field)
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your name'}))
    dob=forms.DateField()
    number=forms.CharField()
    class Meta:
        model=register1
        fields='__all__'
        exclude=['rgid','rid','creates']
    def clean(self):
        cleaned_data=super().clean()
        num=cleaned_data['number']
        if len(num)!=10:
            raise forms.ValidationError('enter valid number')

