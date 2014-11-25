import os
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
		super(Photo, self).save()
		filename = os.path.basename(self.image.path)
		filedir = os.path.dirname(self.image.path)
		if not filename == '':
			img = Image.open(self.image.path)
	    	img.thumbnail((80,80))
	    	img.save("%s%s" % (filedir, '/80x80'+filename))
		
