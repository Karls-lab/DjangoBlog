from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class get_datetime(models.Model):
	now = timezone.now()
	pub_date = models.DateTimeField('date published')
	
	
def get_absolute_url(self):
  return reverse('my_app:my_app', kwargs={'slug': self.slug })
  

class Blog(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	content = models.TextField()
	pub_date = models.DateTimeField('Date Blog Published')
	number_of_comments = models.IntegerField(default=0)
	def __str__(self):
		return self.blog_title


class Comment(models.Model):
	blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	email = models.EmailField()
	content = models.TextField()
	pub_date = models.DateTimeField('Date comment posted')