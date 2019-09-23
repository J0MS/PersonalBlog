from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.http import HttpResponse
from .models import Post
from django.views.defaults import page_not_found
from django.views.generic import ListView, CreateView, UpdateView

def error_404_Post(request, exception):
    data = {"name": "JMPersonalBlog.com"}
    return render(request,'404/index.html', data)

def showAllPost(request):
    all_Post= Post.objects.all()
    context= {'all_Post': all_Post}
    return render(request, '../templates/Home/index.html', context)


class PostList(ListView): 
    model = Post


# Create your views here.
class OnePost(View):
    """
        Displays just one post
    """
    template = 'Post/one_post.html'
    context = {}

    def get(self, request, post_id):
        """
            GET in one post
        """
        # post = Post.objects.get(id=post_id)
        post = get_object_or_404(Post, id=post_id)
        self.context['post'] = post

        self.context['title'] = str(post)

        return render(request, self.template, self.context)
