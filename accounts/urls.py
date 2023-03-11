from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdateView, ProfileDeleteView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path ('profile_update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path ('profile_delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('paypal-return', views.PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancel', views.PaypalCancelView.as_view(), name='paypal-cancel'),
]
