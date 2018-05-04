# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .utils import get_unique_slug

# Create your models here.
# Model for the categories
class Category(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField()
    img_cover = models.ImageField(upload_to='category-img/', null=True)

    """ def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save() """

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "categories"


# Model for the categories
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    # img_header = models.ImageField()

    """ def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save() """

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# Model for our posts
class Post(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True)
    summary = models.TextField(null=True)
    category = models.ForeignKey(Category, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    featured = models.BooleanField()
    HomePage = models.BooleanField()
    img_cover = models.ImageField(upload_to='post-img-covers/', null=True)

    """ def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save() """

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Model for our ads
class Advertisement(models.Model):
    title = models.CharField(max_length=140) 
    slug = models.SlugField(max_length=140, unique=True)
    summary = models.TextField(null=True)
    category = models.ForeignKey(Category, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    featured = models.BooleanField()
    HomePage = models.BooleanField()
    img_cover = models.ImageField(upload_to='adver-img-covers/', null=True)

    """ def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save() """

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Model for our events
class Event(models.Model):
    title = models.CharField(max_length=140) 
    slug = models.SlugField(max_length=140, unique=True)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    place = models.CharField(max_length=250) 
    google_maps = models.CharField(max_length=140)
    summary = models.TextField(null=True)
    category = models.ForeignKey(Category, null=True)
    body = models.TextField()
    price = models.FloatField()
    free = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    Finished = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    HomePage = models.BooleanField(default=False)
    img_cover = models.ImageField(upload_to='event-img-covers/', null=True)

    """ def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save() """

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
    

# Model for our 
class Course_Workshop(models.Model):
    title = models.CharField(max_length=140) 
    slug = models.SlugField(max_length=140, unique=True)
    course = models.BooleanField(default=False)
    workshop = models.BooleanField(default=False)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    place = models.CharField(max_length=250) 
    google_maps = models.CharField(max_length=140)
    summary = models.TextField(null=True)
    category = models.ForeignKey(Category, null=True)
    body = models.TextField()
    price = models.FloatField()
    free = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    Finished = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    HomePage = models.BooleanField(default=False)
    img_cover = models.ImageField(upload_to='course-workshop-img-covers/', null=True)

    """ def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save() """

    class Meta:
        verbose_name_plural = "Courses & Workshops"
        verbose_name = "Course & Workshop"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
