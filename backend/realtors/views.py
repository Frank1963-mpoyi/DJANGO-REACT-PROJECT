from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerializer



class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None # by default any list will be paginated
    
    
class RealtorView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    # no need of pagination bcz it will retreive one object
    
class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None
    
    
def index (request):
    
    obj = Realtor.objects.get(id=1)
    template_name = 'realtor/index.html'
    context = {'obj':  obj }
    return render (request, template_name, context)