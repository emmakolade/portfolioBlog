from django.urls import path
from django.conf import settings
from django.contrib import admin

from .views import Portpage, Blogpage, Postdetail, Contactpage

app_name = "blogP"
urlpatterns = [
    path('', Portpage.as_view(), name= 'portpage'),
    path('blog/', Blogpage.as_view(), name= 'blog'),
    path('post/<int:pk>', Postdetail.as_view(), name= 'post'),
    path('contact/', Contactpage.as_view(), name= 'contact'),




]

# urlpatterns = [
#     path('', views.portpage, name = 'portpage'),
#     path('blog/', views.blogpage, name = 'blog'),
#     path('post/<slug>/', views.post, name = 'post'),
#     path('about/', views.about, name= 'about'),
#     # path('postlist/<slug>/', views.postlist, name = 'postlist'),
#     path('posts/', views.allposts, name = 'allposts'),
#     path('search/', views.search, name = 'search'),
# ]