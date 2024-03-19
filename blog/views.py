from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Comment
from .forms import BlogForm, CommentForm


def home(request):
  blog = Post.objects.all().order_by("-created_on")

  context = {'blogs': blog}
  return render(request, 'home.html', context)
##

def blog_category(request, category):
  blogs = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
  context = {'blogs': blogs, 'category': category}
  return render(request, 'category.html', context)
###
  
def create_blog(request):
  form = BlogForm()

  if form.is_valid():
    form = BlogForm(request.POST)

    blog = Post(
      author = form.cleaned_data['author'],
      title = form.cleaned_data['title'],
      content = form.cleaned_data['content'],
    )
  
    blog.save()
    return HttpResponseRedirect(request.path_info)
  #
  
  context = {'form': BlogForm()}
  return render(request, 'create_blog.html', context)
###

def read_blog(request, pk):
  post = Post.objects.get(pk=pk)
  comment_form = CommentForm()

  if request.method == "POST":
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comments = Comment(
        author=comment_form.cleaned_data["author"],
        body=comment_form.cleaned_data["body"],
        post=post,
      )

      comments.save()
      return HttpResponseRedirect(request.path_info)
  #
  comments = Comment.objects.filter(post=post)
  context = {'blog': post, 'comments': comments, 'form': comment_form}
  return render(request, 'detail.html', context)