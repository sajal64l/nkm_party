from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib.postgres.search import (SearchVector, SearchQuery,
                                            SearchRank)

from django.contrib.auth.models import User

# from account.models import Profile
from .models import Post, Comment
from .forms import CommentForm, SearchForm


from taggit.models import Tag

def post_list(request, tag_slug = None):
    object_list = Post.objects.all()
    latest_posts = Post.objects.order_by('-publish')[:5]
    # Search Functionality
    form = SearchForm()
    query = None
    results = [] 
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') +\
                            SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                rank = SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')

    tag = None
    tag_list = Tag.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6) #6 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'page': page,'posts': posts, 'tag':tag, 'tag_list':tag_list,
               'form': form, 'query': query, 'results': results, 'latest_posts':latest_posts}
    
    return render(request,
                'notice/post/list.html',context)

def post_detail(request, year, month, day, post, tag_slug = None):
    post = get_object_or_404(Post, slug=post,
                                    publish__year = year,
                                    publish__month = month,
                                    publish__day = day)

    # Search Functionality
    form = SearchForm()
    query = None
    results = [] 
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') +\
                            SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                rank = SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')

    tag = None
    tag_list = Tag.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    #List of active comments for this post
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        #A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #Create comment object but don't save to database
           
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            
    else:
        comment_form = CommentForm()
    
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags', '-publish')[:4]
    
    latest_posts = Post.objects.order_by('-publish')[:5]

    context = {'post': post, 'comments': comments, 'new_comment': new_comment,
                'comment_form' : comment_form, 'similar_posts': similar_posts,
                'tag':tag, 'tag_list':tag_list, 'form': form, 'query': query,
                'results': results, 'latest_posts':latest_posts,}
              
    return render(request,
                  'notice/post/detail.html', context)

