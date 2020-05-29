from django import forms
from .models import Activities ,TypeActivities
class AddActtForm(forms.ModelForm , forms.Form):
    title=forms.CharField(label='عنوان النشاط')
    content= forms.CharField(label='نص النشاط', widget=forms.Textarea)
    # type =forms.ModelMultipleChoiceField(queryset=TypeActivities.objects.all())
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta :
        model = Activities
        fields=['title' , 'content' ,'type'] 