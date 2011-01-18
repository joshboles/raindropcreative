from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from work.models import Photo, Project

def index(request):
	project_list = Project.objects.all().order_by('order')
	photos = Photo.objects.all()
	return render_to_response('work/index.html', {'project_list': project_list, 'photos': photos}, context_instance=RequestContext(request))