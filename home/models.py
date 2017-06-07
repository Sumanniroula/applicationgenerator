from django.db import models
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Template(models.Model):
	name = models.CharField(max_length=200)
	content = models.TextField()
	is_published = models.NullBooleanField()
	price = models.FloatField(null = True)
	image = models.ImageField(upload_to='template_images')
	def __str__(self):
		return self.name