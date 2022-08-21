from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import get_datetime
from .models import Blog, Comment

# Create your views here.
now = get_datetime.now

def index(request):
	return render(request, 'blog/index.html', {'now': now})
	
def about(request):
	return render(request, 'blog/about.html', {'now': now})
	
def plan(request):
	return render(request, 'blog/plan.html', {'now': now})
	
def techtips_with_css(request):
	return render(request, 'blog/techtips+css.html', {'now': now})
	
def techtips_without_css(request):
	return render(request, 'blog/techtips-css.html', {'now': now})
	
def useful_hyperlinks(request):
	return render(request, 'blog/useful_hyperlinks.html', {'now': now})
	
def blog_home(request):
	latest_blog_posts = Blog.objects.order_by('pub_date')[:3]
	number_of_comments = 0
	for blog in latest_blog_posts:
		for comment in blog.comment_set.all():
			blog.number_of_comments += 1
	try: 
		title = Blog.objects.get(pk=1)
	except Blog.DoesNotExist:
		raise Http404("Blog does not exist")
	context = {'latest_blog_posts': latest_blog_posts, 'now': now}
	return render(request, 'blog/blog_home.html', context)
	
def blog_entry(request, entry_id):
	blog_entry = Blog.objects.get(pk=entry_id)
	comment_set = blog_entry.comment_set.all()
	number_of_comments = 0
	for element in comment_set:
		number_of_comments += 1
		
	context = {'now': now, 'blog_entry': blog_entry, 'number_of_comments': number_of_comments}
	
	
	if request.method == 'POST':
		post_data = {}
		form = request.POST.dict()
		name = form.get("commenter-name")
		email = form.get("commenter-email")
		content = form.get("commenter-text")
		number_of_comments += 1
		blog_entry.comment_set.create(name=name, email=email, content=content, pub_date=get_datetime.now)
		
		post_data['commenter-name'] = form.get('commenter-name')
		context['data'] = post_data
		context['number_of_comments'] = number_of_comments
		return render(request, 'blog/blog_entry.html', context)
	else:
		return render(request, 'blog/blog_entry.html', context)

	
	
	
def blog_archive(request):
	all_blog_posts = Blog.objects.order_by('pub_date')
	for blog in all_blog_posts:
		for comment in blog.comment_set.all():
			blog.number_of_comments += 1
	context = {'all_blog_posts': all_blog_posts, 'now': now}
	return render(request, 'blog/blog_archive.html', context)
	
	
	
	
	
	