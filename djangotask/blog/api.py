from rest_framework import serializers, viewsets, status as status_code, generics, mixins
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import pagination
from django_filters import rest_framework as filters

class PostFilter(filters.FilterSet):
    created_date = filters.DateFilter(field_name="created_date", lookup_expr='contains')
    published_date = filters.DateFilter(field_name="published_date", lookup_expr='contains')
    text = filters.CharFilter(field_name="text", lookup_expr='icontains')
    # category_text = filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),field_name="category__text",to_field_name="text",widget=CheckboxSelectMultiple(),label="Category",label_suffix="",)
    class Meta:
        model = Post
        fields = ['tag', 'category','author','title','text', 'created_date', 'published_date']

class PostViewSet(viewsets.ModelViewSet	):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('tag', 'category','author','title','text','created_date','published_date')
    filterset_class = PostFilter
    # permission_classes = [permissions.IsAuthenticated] 
    http_method_names = ['get','post','put','patch','delete']

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	http_method_names = ['get','post','put','patch','delete']

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	http_method_names = ['get','post','put','patch','delete']

# class CommentViewSet(viewsets.ModelViewSet):
# 	queryset = Comment.objects.all()
# 	serializer_class = CommentSerializer
# 	http_method_names = ['get','post','put','patch','delete']