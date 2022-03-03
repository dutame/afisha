from django.contrib import admin
from main.models import Director, Category, Genre, Movie, Review, Cinema

# Register your models here.

admin.site.register(Director)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Cinema)
