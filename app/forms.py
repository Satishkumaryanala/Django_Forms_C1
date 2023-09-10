from django import forms

# Create forms here

class StudentForm(forms.Form):
    Sname = forms.CharField()
    Sid = forms.IntegerField()
    Semail = forms.EmailField()
