from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from blog.models import Post, Comment
from .forms import CommentForm

# Create your views here.
def blog_index(request):
    # Grabs QuerySet containing all posts ordered by their creation time
    # - means to start with the most recent post
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    # Grabs posts with categories similar to the arguements given
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk) # Retrieves object with a given pk

    # If POST received, then new instance of a form is created
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save() # Save and add comment to form to context dictionary
            form = CommentForm()
            return HttpResponseRedirect('#')

    comments = Comment.objects.filter(post=post) # Get all comments in a post
    # Posts and comments are added to the context dictionary
    # Rendered to the template
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)

