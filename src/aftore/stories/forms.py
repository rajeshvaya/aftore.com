from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from stories.models import Story


class StoryForm(ModelForm):
	helper = FormHelper()
	helper.form_tag = False
	helper.error_text_inline = True
	helper.label_class = "col-md-2"
	helper.field_class = 'col-md-9'

	class Meta:
		model = Story
		exclude = ('moderator', 'slug', )
		error_messages = {
			'title' :{
				'required' : "Title is required"
			}
		}
