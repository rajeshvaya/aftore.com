import datetime

from django.utils.timezone import utc
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms.models import inlineformset_factory

from stories.models import Story
from stories.forms import StoryForm
from photos.models import Photo
from photos.forms import PhotoForm

def index(request):
	return render(request, 'index.html', {})

def story(request, id=0):
	return render(request, 'stories/story.html', {})

@login_required
def submit(request):
	s = Story()
	PhotoFormSet = inlineformset_factory(Story, Photo, form=PhotoForm, can_delete=False)
	storyform = StoryForm(instance=s)
	photoformset = PhotoFormSet(instance=s)	

	if request.method == 'POST':
		storyform = StoryForm(request.POST)
		if storyform.is_valid():
			pass
	
	return render(request, 'stories/submit.html', {'storyfrom': storyform, 'photoformset': photoformset})

def delete(request):
	pass