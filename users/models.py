from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models import Avg

RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)

class HotelReview(models.Model):
    username = models.TextField()
    hotel_name = models.TextField()
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Hotel Reviews'

    def __str__(self):
        return self.username

    def get_review_rating(self):
        return self.review_rating

class RestaurantReview(models.Model):
    username = models.TextField()
    restaurant_name = models.TextField()
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Restaurant Reviews'

    def __str__(self):
        return self.username

    def get_review_rating(self):
        return self.review_rating

class MovieReview(models.Model):
    username = models.TextField()
    movie_name = models.TextField()
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Movie Reviews'

    def __str__(self):
        return self.username

    def get_review_rating(self):
        return self.review_rating

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        super().save()

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image= models.CharField(max_length=500)
    location= models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    link=models.URLField(max_length = 200, default="https://www.tripadvisor.in/")
    prange=models.TextField(max_length=200, default="2,500-5,000")

    def save(self,*args,**kwargs):
        super(Hotel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image= models.CharField(max_length=500)
    location= models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    link=models.URLField(max_length = 200, default="https://www.tripadvisor.in/")

    def save(self,*args,**kwargs):
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image= models.CharField(max_length=500)
    rating= models.CharField(max_length=100, default='4')
    language= models.CharField(max_length=100)
    Genre=models.CharField(max_length=100)
    link=models.URLField(max_length = 200, default="https://www.imdb.com/")

    def save(self,*args,**kwargs):
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
