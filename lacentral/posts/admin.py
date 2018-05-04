# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Category, Tag, Post, Advertisement, Event, Course_Workshop

# Register your models here
# post
class PostModelAdmin(SummernoteModelAdmin):
    list_display = ['title', 'category', 'updated', 'timestamp', ]
    list_display_links = ['updated']
    list_filter = ['category', 'updated', 'timestamp']
    search_fields = ['title', 'body']
    summernote_fields = ('body',)

admin.site.register(Post, PostModelAdmin)

# advertisement
class AdvertisementModelAdmin(SummernoteModelAdmin):
    list_display = ['title', 'category', 'updated', 'timestamp', ]
    list_display_links = ['updated']
    list_filter = ['category', 'updated', 'timestamp']
    search_fields = ['title', 'body']
    summernote_fields = ('body',)

admin.site.register(Advertisement, AdvertisementModelAdmin)

# event
class EventModelAdmin(SummernoteModelAdmin):
    list_display = ['title', 'category', 'updated', 'timestamp', ]
    list_display_links = ['updated']
    list_filter = ['category', 'updated', 'timestamp']
    search_fields = ['title', 'body']
    summernote_fields = ('body',)

admin.site.register(Event, EventModelAdmin)

# course & workshop
class Course_WorkshopModelAdmin(SummernoteModelAdmin):
    list_display = ['title', 'category', 'updated', 'timestamp', ]
    list_display_links = ['updated']
    list_filter = ['category', 'updated', 'timestamp']
    search_fields = ['title', 'body']
    summernote_fields = ('body',)

admin.site.register(Course_Workshop, Course_WorkshopModelAdmin)

# category
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    search_fields = ['name',]

admin.site.register(Category, CategoryModelAdmin)

# tags
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    search_fields = ['name',]

admin.site.register(Tag, TagModelAdmin)
