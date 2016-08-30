from django import forms
from .validators import validate_file_extension

class UploadFileForm(forms.Form):
	file = forms.FileField(validators=[validate_file_extension])
	change_word = forms.CharField(max_length=50)
	to = forms.CharField(max_length=50)
