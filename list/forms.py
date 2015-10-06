from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100),

#your_school = forms.CharField(label='Your school', max_length=100),

#your_data = forms.CharField(label='Your data', max_length=100)

class infoForm(forms.Form):
	data = forms.CharField(label = 'data'),
	createDate = forms.DateTimeField('date published'),
	ownerName = forms.CharField(max_length = 200),
	priority = forms.IntegerField(initial = 10),
	dropOffLocation = forms.CharField(max_length = 200),
	uniqueID = forms.IntegerField(initial = 0),
