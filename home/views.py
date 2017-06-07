from django.shortcuts import render
from django.http import HttpResponse
from .models import Template
from weasyprint import HTML
from .core import ContentHandler
from weasyprint import HTML,CSS

def home(request):
	templates = Template.objects.all()[:10]
	return render(request , 'index.html',{'templates':templates})


def contents(request,template_id):
	template = Template.objects.get(pk=template_id)
	return render(request , 'home/contents.html',{'template':template})


def edit(request,template_id):
	template = Template.objects.get(pk=template_id)
	contentHandler = ContentHandler();
	fields = contentHandler.getAllFields(template.content)
	return render(request , 'home/edit.html',{'template':template , 'fields' : fields})
	return render(request, 'home/googleapi.html', {'fields':fields})

def generate(request,template_id):
	template = Template.objects.get(pk=template_id)
	myDict = request.POST.copy()
	del myDict['csrfmiddlewaretoken']
	contentHandler = ContentHandler();

	htmlstring = contentHandler.replace(template.content,myDict)

	html = HTML(string=htmlstring)
	main_doc = html.render()
	pdf = main_doc.write_pdf()
	return HttpResponse(pdf, content_type='application/pdf')
