from django.urls import path 
from .views import (
    RealtorListView,
    RealtorView,
    TopSellerView, 
    index )



urlpatterns = [
    path('index', index),
    path('', RealtorListView.as_view()),
    path('<int:pk>',  RealtorView.as_view(), name=""),
    path('topseller', TopSellerView.as_view(), name="" ),
]

