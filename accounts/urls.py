from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path ('profile_update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path ('profile_delete/', ProfileDeleteView.as_view(), name='profile_delete'),

]
