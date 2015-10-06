from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime

from django.template.context_processors import csrf

from .forms import infoForm

from .models import listObject


def index(request):
	return render(request, 'list/index.html')

def entry(request):
	c = {}
	c.update(csrf(request))

#newEntry = infoForm()
	
	return render_to_response('list/entry.html', c)

def nextPrints(request):
	next_five_prints = listObject.objects.order_by('createDate')
	context = {'next_five_prints' : next_five_prints}
	return render(request, 'list/nextPrints.html', context)

def confirm(request):
	return render(request, 'list/confirm.html')

def detail(request, question_id):
	info = get_object_or_404(listObject, pk=question_id)
	return render(request, 'list/detail.html', {'info': info})

def get_name(request):
	
	
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = infoForm(request.POST)
	# check whether it's valid:
		if form.is_valid():
		# process the data in form.cleaned_data as required
			newEntry = listObject(**form.cleaned_data)
			#datum = request.POST.get('data')
			#testString = form.cleaned_data['data']
			#print datum
			#print form.cleaned_data.get('data')
			newEntry.data = request.POST.get('data')
			newEntry.ownerName = request.POST.get('ownerName')
			newEntry.dropOffLocation = request.POST.get('dropOffLocation')
			newEntry.createDate = datetime.now()
			newEntry.save()
		# redirect to a new URL:
			return HttpResponseRedirect('/list/confirm/')
			
			# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()
					
	return render(request, 'list/name.html', {'form': form})