"""user_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import CustomLoginView  
from users.forms import LoginForm
from users.views import ResetPasswordView
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from users.views import ChangePasswordView
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # This is what we added
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('restaurants/', user_views.restaurants, name="restaurants"),
    path('hotels/', user_views.hotels, name="hotels"),
    path('movies/', user_views.movies, name="movies"),
    path('home/', user_views.home, name="home"),
    path('api_h/get/', user_views.api_h, name="api"),
    path('api_r/get/', user_views.api_r, name="api"),
    path('api_m/get/', user_views.api_m, name="api"),
    path('hotelreviews/', user_views.hotelreviews, name="hotelreviews"),
    path('restaurantreviews/', user_views.restaurantreviews, name="restaurantreviews"),
    path('moviereviews/', user_views.moviereviews, name="moviereviews"),
    path('userhotelreviews/', user_views.userhotelreviews, name="userhotelreviews"),
    path('userrestaurantreviews/', user_views.userrestaurantreviews, name="userrestaurantreviews"),
    path('usermoviereviews/', user_views.usermoviereviews, name="usermoviereviews"),
    path('search_r/', user_views.search_r, name = "search_r"),
    path('search_h/', user_views.search_h, name = "search_h"),
    path('search_m/', user_views.search_m, name = "search_m"),
    path('load_h/', user_views.load_h, name = "load_h"),
    path('load_r/', user_views.load_r, name = "load_r"),
    path('load_m/', user_views.load_m, name = "load_m"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

