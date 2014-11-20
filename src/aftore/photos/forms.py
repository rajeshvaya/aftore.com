from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from photos.models import Photo

class PhotoForm(ModelForm):
	helper = FormHelper()
	helper.form_tag = False
	helper.error_text_inline = True
	helper.label_class = "col-md-2"
	helper.field_class = 'col-md-9'

	class Meta:
		model = Photo
		exclude = ('story','name')
		error_messages = {
			'image' :{
				'required' : "You must upload at least one photo"
			}
		}
