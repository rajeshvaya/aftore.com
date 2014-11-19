import datetime

from django.utils.timezone import utc
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from stories.models import Story

def index(request):
	return render(request, 'index.html', {})

def story(request, id=0):
	return render(request, 'stories/story.html', {})

@login_required
def submit(request):
	return render(request, 'stories/submit.html', {})

def delete(request):
	pass