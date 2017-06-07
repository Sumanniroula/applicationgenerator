from django.contrib import admin
from .models import Template
from django import forms
from ckeditor.widgets import CKEditorWidget



class TemplateAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	# name = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Template
		fields = '__all__'

class TemplateAdmin(admin.ModelAdmin):
	form = TemplateAdminForm
	# list_display = ('name','content')



admin.site.register(Template,TemplateAdmin)



