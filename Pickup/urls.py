from django.urls import path
from .views import PickupView, PickupRetriveView
urlpatterns = [
    path('pickup/', PickupView.as_view(), name='pickup'),
    path('pickup/<str:rcNo>/', PickupView.as_view(), name='pickup'),
    path('pickuplist', PickupRetriveView.as_view(), name='pickuplist'),

]
