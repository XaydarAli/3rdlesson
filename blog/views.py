from django.shortcuts import render,redirect
from django.views import View
from blog.models import Post
from blog.forms import  PostForm
from django.views.generic import ListView,DetailView
from django.contrib import messages
from django.core.paginator import Paginator

# class PostListView(ListView):
#     model =Post
#     template_name = "blog.html"
#     context_object_name = "posts"
# def post_list(request):
#     post = Post.objects.all()
#     return render(request, 'blog.html', {'post': post})
class PostView(View):
    def get(self,request):
        posts=Post.objects.all().order_by('id')
        pagination=Paginator(posts,1)
        page = request.GET.get('page', 1)
        pages = pagination.get_page(page)
        context={"pages":pages}
        return render(request,"blog.html",context)
class PostDetailView(DetailView):
    model =Post
    pk_url_kwarg = "id"
    template_name = "blog-detail.html"
    context_object_name = "post"