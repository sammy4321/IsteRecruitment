from django import forms

class Infoform(forms.Form):
	Name = forms.CharField(max_length=140)
	Number = forms.IntegerField()
