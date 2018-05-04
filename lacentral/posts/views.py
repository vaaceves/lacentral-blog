# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Category, Tag, Post, Advertisement

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.template import defaultfilters
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.template import loader
from django.http import HttpResponse
from django.views.generic.base import View
from django.db.models import Q

# Create your views here.
# post
def post_view(request, slug_post):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-id')[:5]
    context = {
        'categories_list': categories,
        'tags_list': tags,
        'posts_list': posts
    }
    try:
        post = Post.objects.get(slug=slug_post)
        categoy_post = post.category
        category_posts = Post.objects.filter(category=categoy_post).order_by('-id')[:3]
        context['this_post'] = post
        context['category_posts_list'] = category_posts
    
    except Post.DoesNotExist:
        context['this_post'] = None
        context['category_posts_list'] = None

    return render(request, 'posts/this_post.html', context)


# category
def category_view(request, slug_category):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-id')[:5]
    context = {
        'categories_list': categories,
        'tags_list': tags,
        'posts_list': posts
    }
    try:
        category = Category.objects.get(slug=slug_category)
        category_posts = Post.objects.filter(category=category)
        context['this_category'] = category
        context['this_category_posts'] = category_posts
    
    except Category.DoesNotExist:
        context['this_category'] = None
        context['this_category_posts'] = None

    return render(request, 'posts/this_category.html', context)