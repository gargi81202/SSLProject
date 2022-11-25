# SSL-Project
Repository for the course project done as part of CS-251 (Software Systems Lab) course at IIT Bombay in Autumn 2022.
ReviewPool is a Service Rating Website for Hotels, Movies and Restaurants
## TECH STACK
* Languages: Python, Javascript, HTML
* Backend: Django
* Frontend: HTML, CSS, Bootstrap, FontAwesome, Vue.js
## TEAM
* Gargi Bakshi 
* Moningi Srija
* Somidi Sathwika Reddy
## KEY FEATURES
### USER-AUTHENTICATION
We created register user, login forms using django.contrib.auth for authentication and tokenization of users. There is a feature for changing password
### DASHBOARD
Dashboard is the home page of our website in which a user can navigate to different pages, visit their profile page and logout.
### PROFILE
This is the profile page of user containing the user's personal information and their reviews for various hotels, restaurants and movies.
### HOTELS, RESTAURANTS AND MOVIES
The user can access any page which displays suggested hotels, restaurants or movies, which are sorted according to rating initially. 
#### SEARCH BAR
The user can search for a hotel, city or any keyword to get the hotels, restaurants or movies related to it.
#### FILTERS
The user can filter results using the filters provided
* Hotels: Location, Rating
* Movies: Language, Genre
* Restaurants: Location, Rating
### DISPLAY
The hotels, movies and restaurants are displayed as cards containing information about them. Each card has a button allowing the user to write a review.
* Hotels
    * Image
    * Description
    * Rating
    * Location
    * Price Range
    * Add Review Button
* Movies
    * Poster
    * Description
    * Rating
    * Language
    * Genre
    * Add Review Button
* Restaurants
    * Image
    * Description
    * Rating
    * Location
    * Add Review Button
### REVIEWS
The user can add their review for a hotel, restaurant or movie by clicking on the "Add review" button and fill the form which gets displayed in the Users Reviews Page. There are three seperate pages of reviews for hotels, movies and restaurants made by the user which can be accessed through the user's profile page.
## BASIC COMMANDS
Run these commands in the folder containing manage.py
```
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```


