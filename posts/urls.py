from django.urls import path
from . import views

urlpatterns = [

    path('', views.PostList.as_view(), name='list'),
    path('drafts/', views.DraftList.as_view(), name='drafts'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('post/new/', views.PostCreate.as_view(), name='create'),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name='update'),
    path('post/<int:pk>/remove/', views.PostDelete.as_view(), name='delete'),
]
    
