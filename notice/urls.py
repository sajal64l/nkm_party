from django.urls import path
from .feeds import LatestPostsFeed
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail, 
        name='post_detail'),
    
    path('tag/<slug:tag_slug>/', 
         views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]