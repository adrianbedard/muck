# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from muck.maker.models import Document, Info
from muck.maker.forms import DocumentForm, infoForm

def home(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/home.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )


def upload(request):
	# Handle file upload
	
	passwordMaster = "prints"
	
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		info = infoForm(request.POST, request.FILES)
		if form.is_valid() and info.is_valid():
			
			newInfo = Info()
			newInfo.password = request.POST.get('password')
			print(newInfo.password)
			if(passwordMaster == newInfo.password):
				
				print("Passed")
				newdoc = Document(docfile = request.FILES['docfile'])
			
			
				newdoc.save()
			
			
				newInfo.ownerName = request.POST['ownerName']
				newInfo.schoolName = request.POST.get('schoolName')
				newInfo.datum = request.FILES['docfile']
			
				newInfo.save()
				
				# Redirect to the document list after POST
				return HttpResponseRedirect(reverse('muck.maker.views.home'))
			else:
				print("Failed")
				form = DocumentForm()
				info = infoForm()
	else:
		form = DocumentForm() # A empty, unbound form
		info = infoForm()

							
	# Load documents for the list page
	documents = Document.objects.all()
	infos = Info.objects.all()
								# Render list page with the documents and the form
	return render_to_response(
		'maker/upload.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
		context_instance=RequestContext(request)
	)

def printout(request, question_id):
	infoToPrint = get_object_or_404(Info, pk=question_id)
	return render(request, 'maker/printout.html', {'infoToPrint': infoToPrint})

def about_tools(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/about_tools.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )

def about_curriculum(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/about_curriculum.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )

def about_staff(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/about_staff.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )

def watch(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/watch.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )


def tips_3D(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/tips_3D.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )


def tips_laser(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/tips_laser.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )

def contact(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/contact.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )

def Prints(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()

	return render_to_response(
							  'maker/Prints.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )

def list(request):
	form = DocumentForm() # A empty, unbound form
	info = infoForm()
	documents = Document.objects.all()
	infos = Info.objects.all()
	
	return render_to_response(
							  'maker/list.html',
							  {'documents': documents, 'form': form, 'infos': infos, 'info': info},
							  context_instance=RequestContext(request)
							  )
