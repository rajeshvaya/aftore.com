from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from photos.models import Photo

class PhotoForm(ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(PhotoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_tag = False
		self.helper.label_class = "col-md-2"
		self.helper.field_class = 'col-md-9'

	class Meta:
		model = Photo
		exclude = ('story','name')
		error_messages = {
			'image' :{
				'required' : "You must upload at least one photo"
			}
		}
