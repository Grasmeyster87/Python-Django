# from django.db import models
from tastypie.resources import ModelResource
from shop.models import Category, Course

# Create your models here.

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.object.all()
        resource_name = 'categories'
        allowed_methods = ['get']
    
class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
