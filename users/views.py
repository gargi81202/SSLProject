from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm, AddHotelReview, AddRestaurantReview, AddMovieReview
import requests
import json
from django.http import JsonResponse
from .models import Hotel, Restaurant, Movie, HotelReview, RestaurantReview, MovieReview

def hotelreviews(request):
    form=AddHotelReview(request.POST, instance=request.user)
    context={"form":form}
    # true_username = request.user.username
    if request.method == 'POST':
        if form.is_valid():
            rt=form.cleaned_data['review_text']
            rr=form.cleaned_data['review_rating']
            # un = request.user.username
            # print(un)
            # print(request.user.username)
            hn = form.cleaned_data['hotel_name']
            review=HotelReview(username = request.user.username, hotel_name = hn, review_text=rt, review_rating=rr)
            review.save()
    context = { 'form': form, 'user':request.user}
    return render(request, 'users/hotelreviews.html', context)

def restaurantreviews(request):
    form=AddRestaurantReview(request.POST, instance=request.user)
    context={"form":form}
    if request.method == 'POST':
        if form.is_valid():
            rt=form.cleaned_data['review_text']
            rr=form.cleaned_data['review_rating']
            # un = form.cleaned_data['username']
            rn = form.cleaned_data['restaurant_name']
            review=RestaurantReview(username = request.user.username, restaurant_name = rn, review_text=rt, review_rating=rr)
            review.save()
    context = { 'form': form, 'user':request.user}
    return render(request, 'users/restaurantreviews.html', context)

def moviereviews(request):
    form=AddMovieReview(request.POST, instance=request.user)
    context={"form":form}
    if request.method == 'POST':
        if form.is_valid():
            rt=form.cleaned_data['review_text']
            rr=form.cleaned_data['review_rating']
            # un = form.cleaned_data['username']
            mn = form.cleaned_data['movie_name']
            review=MovieReview(username = request.user.username, movie_name = mn, review_text=rt, review_rating=rr)
            review.save()
    context = { 'form': form, 'user':request.user}
    return render(request, 'users/moviereviews.html', context)

def userhotelreviews(request):
    htlrvwlst = []
    f = HotelReview.objects.all()
    for d in f:
        # print(d.username)
        if d.username == request.user.username:
            htlrvwlst.append(d)
    return render(request, 'users/userhotelreviews.html', {'htlrvwlst':htlrvwlst})

def userrestaurantreviews(request):
    rstrntrvwlst = []
    f = RestaurantReview.objects.all()
    for d in f:
        if d.username == request.user.username:
            rstrntrvwlst.append(d)
    return render(request, 'users/userrestaurantreviews.html', {'rstrntrvwlst':rstrntrvwlst})

def usermoviereviews(request):
    mvrvwlst = []
    f = MovieReview.objects.all()
    for d in f:
        if d.username == request.user.username:
            mvrvwlst.append(d)
    return render(request, 'users/usermoviereviews.html', {'mvrvwlst':mvrvwlst})

def hotels(request):
    hotel_objs = Hotel.objects.all()
    return render(request, 'users/hotels.html', {'hotel_objs': hotel_objs})

def restaurants(request):
    restaurant_objs = Restaurant.objects.all()
    return render(request, 'users/restaurants.html', {'restaurant_objs': restaurant_objs})

def movies(request):
    movie_objs = Movie.objects.all()
    return render(request, 'users/movies.html', {'movie_objs': movie_objs})

def api_h(request):
    hotel_objs=Hotel.objects.order_by('-rating')
    location=request.GET.get('location')
    rating=request.GET.get('rating')
    # print(location)
    # print(rating)
    payload=[]
    for hotel_obj in hotel_objs:
        result={}
        result['name']=hotel_obj.name
        result['image']=hotel_obj.image
        result['description']=hotel_obj.description
        result['rating']=hotel_obj.rating
        result['link']=hotel_obj.link
        result['location']=hotel_obj.location
        result['prange']=hotel_obj.prange
        payload.append(result)
        if location and rating:
            if result['location']!=location or float(result['rating'])<float(rating):
                payload.pop()
    return JsonResponse(payload, safe=False)

def api_r(request):
    restaurant_objs=Restaurant.objects.order_by('-rating')
    location=request.GET.get('location')
    rating=request.GET.get('rating')
    payload=[]
    for restaurant_obj in restaurant_objs:
        result={}
        result['name']=restaurant_obj.name
        result['image']=restaurant_obj.image
        result['description']=restaurant_obj.description
        result['rating']=restaurant_obj.rating
        result['link']=restaurant_obj.link
        result['location']=restaurant_obj.location
        payload.append(result)
        if result['location']!=location or float(result['rating'])<float(rating):
            payload.pop()
    return JsonResponse(payload, safe=False)

def api_m(request):
    movie_objs=Movie.objects.order_by('-rating')
    language=request.GET.get('language')
    genre=request.GET.get('Genre')
    # print(language)
    # print(genre)
    payload=[]
    for movie_obj in movie_objs:
        result={}
        result['name']=movie_obj.name
        result['image']=movie_obj.image
        result['description']=movie_obj.description
        result['rating']=movie_obj.rating
        result['language']=movie_obj.language
        result['link']=movie_obj.link
        result['Genre']=movie_obj.Genre
        payload.append(result)
        if language and genre:
            if result['language']!=language or result['Genre']!=genre:
                payload.pop()
    return JsonResponse(payload, safe=False)

def search_r(request):
    # print("called")
    restaurant_objs=Restaurant.objects.order_by('-rating')
    keyword=request.GET.get('keyword')
    # print(keyword)
    payload=[]
    for restaurant_obj in restaurant_objs:
        result={}
        result['name']=restaurant_obj.name
        result['image']=restaurant_obj.image
        result['description']=restaurant_obj.description
        result['rating']=restaurant_obj.rating
        result['link']=restaurant_obj.link
        result['location']=restaurant_obj.location
        payload.append(result)
        if not (keyword in result['name'].lower()) and not(keyword in result['description'].lower()) and not(keyword in result['location'].lower()):
            payload.pop()
    return JsonResponse(payload, safe=False)

def search_h(request):
    # print("called")
    restaurant_objs=Hotel.objects.order_by('-rating')
    keyword=request.GET.get('keyword')
    keyword=keyword.lower()
    # print(type(keyword))
    payload=[]
    for restaurant_obj in restaurant_objs:
        result={}
        result['name']=restaurant_obj.name
        result['prange']=restaurant_obj.prange
        result['image']=restaurant_obj.image
        result['description']=restaurant_obj.description
        result['rating']=restaurant_obj.rating
        result['link']=restaurant_obj.link
        result['location']=restaurant_obj.location
        payload.append(result)
        if not (keyword in result['name'].lower()) and not(keyword in result['description'].lower()) and not(keyword in result['location'].lower()):
            payload.pop()
    return JsonResponse(payload, safe=False)

def search_m(request):
    # print("called")
    movie_objs=Movie.objects.order_by('-rating')
    keyword=request.GET.get('keyword')
    # print(keyword)
    payload=[]
    for movie_obj in movie_objs:
        result={}
        result['name']=movie_obj.name
        result['image']=movie_obj.image
        result['description']=movie_obj.description
        result['rating']=movie_obj.rating
        result['Genre']=movie_obj.Genre
        result['link']=movie_obj.link
        result['language']=movie_obj.language
        payload.append(result)
        if not (keyword in result['name'].lower()) and not(keyword in result['description'].lower()) and not(keyword in result['Genre'].lower()):
            payload.pop()
    return JsonResponse(payload, safe=False)
   

def load_m(request):
    movie_objs=Movie.objects.order_by('-rating')
    payload=[]
    for movie_obj in movie_objs:
        result={}
        result['name']=movie_obj.name
        result['image']=movie_obj.image
        result['description']=movie_obj.description
        result['rating']=movie_obj.rating
        result['link']=movie_obj.link
        result['Genre']=movie_obj.Genre
        result['language']=movie_obj.language
        payload.append(result)
    return JsonResponse(payload, safe=False)

def load_r(request):
    restaurant_objs=Restaurant.objects.order_by('-rating')
    payload=[]
    for restaurant_obj in restaurant_objs:
        result={}
        result['name']=restaurant_obj.name
        result['image']=restaurant_obj.image
        result['link']=restaurant_obj.link
        result['description']=restaurant_obj.description
        result['rating']=restaurant_obj.rating
        result['location']=restaurant_obj.location
        payload.append(result)
    return JsonResponse(payload, safe=False)

def load_h(request):
    hotel_objs=Hotel.objects.order_by('-rating')
    payload=[]
    for hotel_obj in hotel_objs:
        result={}
        result['name']=hotel_obj.name
        result['image']=hotel_obj.image
        result['description']=hotel_obj.description
        result['link']=hotel_obj.link
        result['rating']=hotel_obj.rating
        result['prange']=hotel_obj.prange
        result['location']=hotel_obj.location
        payload.append(result)
    return JsonResponse(payload, safe=False)



class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'
    
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})
        
def home(request):
    return render(request, 'users/home.html')


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')
