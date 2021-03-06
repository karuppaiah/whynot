from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from polls.serializers import UserSerializer, GroupSerializer, ProductSerializer,ProductFeedSerializer
from django.shortcuts import render
from django.http import HttpResponse
from productentity.models import Productdata,Productfeed

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProductdataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Productdata.objects.all()
    serializer_class = ProductSerializer

class ProductfeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Productfeed.objects.all()
    serializer_class = ProductFeedSerializer