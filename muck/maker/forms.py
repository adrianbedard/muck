# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

class infoForm(forms.Form):
	ownerName = forms.CharField(label = 'Name'),
	schoolName = forms.CharField(label = 'School'),
	password = forms.CharField(label = 'Password'),
