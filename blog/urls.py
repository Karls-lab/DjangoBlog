from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'blog'
urlpatterns = [
	path('blog_home', views.blog_home, name='blog_home'),
	path('', views.blog_home, name='blog_home'),
	path('<int:entry_id>/', views.blog_entry, name='blog_entry'),
	path('blog_archive.html/', views.blog_archive, name='blog_archive'),
	path('about.html/', views.about, name='about'),
	path('plan.html/', views.plan, name='plan'),
	path('techtips+css.html/', views.techtips_with_css, name='techtips+css'),
	path('techtips-css.html/', views.techtips_without_css, name='techtips-css'),
	path('useful_hyperlinks.html/', views.useful_hyperlinks, name='useful_hyperlinks'),
]