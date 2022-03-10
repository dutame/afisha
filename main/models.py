from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class Director(models.Model):
    class Meta:
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'

    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.TextField(null=True, blank=True, verbose_name='Биография')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'

    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    title = models.CharField(max_length=255, verbose_name='Название фильма')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, verbose_name='Кинотеатр')
    price_ticket = models.FloatField(verbose_name='Стоимость билета', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    genre = models.ForeignKey(Genre, related_name='movie_genre', on_delete=models.CASCADE, null=True,
                              verbose_name='Жанры')
    director = models.ForeignKey(Director, related_name='movie_director', on_delete=models.CASCADE, null=True,
                                 verbose_name='Режиссёр')
    price = models.FloatField(verbose_name='Купить онлайн трансляцию', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'Рецензии'
        verbose_name_plural = 'Рецензия'

    title = models.CharField(max_length=255, null=True, verbose_name='Название фильма')
    description = models.TextField(null=True, blank=True, verbose_name='Рецензия')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, verbose_name='Фильм')

    def __str__(self):
        return self.description
