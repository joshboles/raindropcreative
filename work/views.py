from django.shortcuts import render_to_response
from django.template import RequestContext
from work.models import Project

def index(request):
	project_list = Project.objects.all()
	return render_to_response('work/index.html', {'project_list': project_list}, context_instance=RequestContext(request))