from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        #fields = ['full_name', 'email', 'age']
        exclude = ['last_update']
        model = Student

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 120:
            raise forms.ValidationError('you maybe too old for this class')

        elif age < 10:
            raise forms.ValidationError('you maybe too young for this class')
        return age


class FeedbackForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message == 'Dirty':
            message == 'Clean'
        return message