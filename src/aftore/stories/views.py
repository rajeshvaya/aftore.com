import datetime

from django.utils.timezone import utc
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms.models import formset_factory

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
	PhotoFormSet = formset_factory(PhotoForm, extra=4)
	if request.method == 'POST':
		storyform = StoryForm(request.POST, request.FILES)
		photoformset = PhotoFormSet(request.POST)	
		print photoformset.is_valid()
		if storyform.is_valid() and photoformset.is_valid():
			s = Story(
				title = storyform.cleaned_data['title'],
				moderator = request.user
			)
			s.save();
	else:
		storyform = StoryForm()
		photoformset = PhotoFormSet()	


	
	return render(request, 'stories/submit.html', {'storyfrom': storyform, 'photoformset': photoformset})

def delete(request):
	pass