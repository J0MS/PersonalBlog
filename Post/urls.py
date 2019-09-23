from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls import url, include
# from django.conf.urls import handler404
from Post.views import showAllPost, PostList
# handler404 = error_404_Post

urlpatterns = [
    path('<int:post_id>/', views.OnePost.as_view(), name='onePost'),
    url(r'^listar', showAllPost, name='post_listar'),
]


 
