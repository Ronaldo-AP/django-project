from django.urls import path
from . import views


urlpatterns = [
    
    path('',        views.CustomLoginView.as_view(),    name='login'),
    path('login/',  views.CustomLoginView.as_view(),    name='login'),
    path('signup/', views.CustomSignUpView.as_view(),   name='signup'),

    path('feed/',   views.feedView,     name='feed'),
    path('logout/', views.logoutView,   name='logout'),

    # path('profile/<str:username>/', views.profileView, name='profile'),
]