from django import forms
from .models import username 


class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'
		widgets = {
			'address': forms.Textarea(attrs={'rows': '5',
											 'cols': '10'})
		}
