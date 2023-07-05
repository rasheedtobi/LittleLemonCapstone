from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuItemSerializer


# Create your views here. 
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
