from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('create_blog', views.create_blog, name="create_blog"),
  path('blog/<int:pk>', views.read_blog, name="read_blog"),
  path('category/<category>', views.blog_category, name="blog_category"),
]
