from PIL import Image

from django.db import models

from stories.models import Story

class Photo(models.Model):
	name = models.CharField(max_length=128)
	image = models.ImageField(upload_to='user_photos')
	story = models.ForeignKey(Story)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
	updated_at = models.DateTimeField(auto_now=True)

	def save(self):
		filename = self.get_image_filename()
		if not filename == '':
			img = Image.open(filename)
	    	img.thumbnail((512,512), Image.ANTIALIAS)
	    	img.save(self.get_medium_filename())
	    	img.thumbnail((80,80), Image.ANTIALIAS)
	    	img.save(self.get_small_filename())
		super(Photo, self).save()
