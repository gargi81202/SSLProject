from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Hotel)
admin.site.register(Restaurant)
admin.site.register(Movie)
admin.site.register(HotelReview)
admin.site.register(RestaurantReview)
admin.site.register(MovieReview)