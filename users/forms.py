from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, HotelReview, RestaurantReview, MovieReview

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

class AddHotelReview(forms.ModelForm):
    # username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control',}))
    hotel_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control',}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
    class Meta:
        model = HotelReview
        fields = ['hotel_name', 'review_text', 'review_rating']

class AddRestaurantReview(forms.ModelForm):
    # username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control',}))
    restaurant_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control',}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
    class Meta:
        model = RestaurantReview
        fields = [ 'restaurant_name', 'review_text', 'review_rating']

class AddMovieReview(forms.ModelForm):
    # username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control',}))
    movie_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control',}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
    class Meta:
        model = MovieReview
        fields = [ 'movie_name', 'review_text', 'review_rating']