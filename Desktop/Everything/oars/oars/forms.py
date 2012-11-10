from django import forms
from oars_website.models import CourseOffer
from oars_website.views import *

class RegistrationForm(forms.Form):
	course = forms.ModelChoiceField(queryset = CourseOffer.objects.all(), empty_label=None)