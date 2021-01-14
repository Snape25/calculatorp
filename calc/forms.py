from django import forms

class StudentForm(forms.Form):  
    height= forms.IntegerField()  
    weight  = forms.IntegerField()  