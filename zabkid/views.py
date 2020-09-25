from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .serializers import Online_RideSerializer
from .models import Online_Ride
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django_filters import rest_framework as filters
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

from .serializers import *

def index(request):
    return render(request,'index.html')


class Online_RideViewSet(GenericViewSet,  # generic view functionality
                         CreateModelMixin,  # handles POSTs
                         RetrieveModelMixin,  # handles GETs for 1 Company
                         UpdateModelMixin,  # handles PUTs and PATCHes
                         ListModelMixin):  # handles GETs for many Companies
    serializer_class = Online_RideSerializer
    queryset = Online_Ride.objects.all()
    filterset_fields = ['parent_id']


class DriverAPI(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact_number']


class ChildrensAPI(viewsets.ModelViewSet):
    queryset = Childrens.objects.all()
    serializer_class = ChildrensSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parent', 'id']


class AddAssignDriverAPI(viewsets.ModelViewSet):
    serializer_class = AddAssign_DriverSerializer
    queryset = Assign_driver.objects.all()


class AssignDriverAPI(viewsets.ModelViewSet):
    queryset = Assign_driver.objects.all()
    serializer_class = Assign_DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['driver_id', 'children_id']


class RideHistoryAPI(viewsets.ModelViewSet):
    queryset = Ride_history.objects.all()
    serializer_class = Ride_historySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parent_id']


class ADDRideHistoryAPI(viewsets.ModelViewSet):
    queryset = Add_Ride_history.objects.all()
    serializer_class = Add_Ride_historySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parent_id']


class ParentAPI(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contactno']


class ShiftsAPI(viewsets.ModelViewSet):
    serializer_class = ShiftsSerializer
    queryset = Shifts.objects.all()[:5]


class getDriver1(generics.ListAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        username = self.request.query_params.get('contact_number', None)
        if username is not None:
            queryset = queryset.filter(Driver__contact_number=username)
        return queryset


class getDriver(APIView):
    serializer_class = DriverSerializer

    def get(self, request, id):
        queryset = Driver.objects.filter(pk=id)
        return queryset


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
