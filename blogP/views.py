from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Project
from datetime import datetime, date
from django.db.models import Q
# Create your views here.

class Portpage(ListView):
    model = Project
    template_name = 'store/index.html'
    ordering = ['-date']

    # def get_queryset(self):
    #     # original qs
    #     qs = super().get_queryset() 
    #     # filter by a variable captured from url, for example
    #     return qs.filter(name__startswith=self.kwargs['portpage'])
    
# def portpage(request):
#     return render(request, 'store/index.html')

class Blogpage(ListView):
    model = Post 
    template_name = 'store/blog.html'
    ordering = ['-id']
    
# def blogpage(request):
#     categories = Category.objects.all()[0:3]
#     featured = Post.objects.filter()
#     latest = Post.objects.order_by('-time_posted')[0:3]
#     context = {
#         'object_list' : featured,
#         'latest' : latest,
#         'categories' : categories,
#     }
#     return render(request, 'store/blog.html', context)

class Postdetail(DetailView):
    model = Post
    template_name = 'store/post.html'
    # pk_url_kwarg = "post_id"

class Contactpage(ListView):
    model = Post
    template_name = 'store/contact.html'


# def post(request, slug):
#     post = Post.objects.get(slug=slug)
#     latest = Post.objects.order_by('-time_posted')[:3]
#     context = {
#         'post' : post,
#         'latest' : latest,
#     }
#     return render(request, 'store/post.html', context)


# def about(request):
#     return render(request, 'store/about.html')

# def category_post_list (request, slug):
#     category = Category.objects.get(slug = slug)
#     posts = Post.objects.filter(categories__in=[category])
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'post_list.html', context)

# def allposts(request):
#     posts = Post.objects.order_by('-time_posted')
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'all_posts.html', context)

# search logic
# def search(request):
#     queryset = Post.objects.all()
#     query = request.Get.get('q')
#     if query:
#         queryset = queryset.filter(
#             Q(title__icontains=query) | Q(overview__icontains=query)
#         ).distinct()
#     context = {
#         'queryset' : queryset
#     }
#     return render(request, 'search_bar.html', context)