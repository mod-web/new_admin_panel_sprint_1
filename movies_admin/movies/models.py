from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('Жанр'), max_length=100)
    description = models.TextField(_('Описание'), blank=True, null=True)

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')
        db_table = "content\".\"genre"

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('Полное имя'), max_length=255)

    class Meta:
        verbose_name = _('Персона')
        verbose_name_plural = _('Персоны')
        db_table = "content\".\"person"

    def __str__(self):
        return self.full_name


class Filmwork(UUIDMixin, TimeStampedMixin):
    class TypeFilmwork(models.TextChoices):
        MOVIE = 'M', _('Фильм')
        TV_SHOW = 'T', _('ТВ шоу')

    title = models.CharField(_('Название'), max_length=255)
    description = models.TextField(_('Описание'), blank=True, null=True)
    creation_date = models.DateField(_('Дата выхода'), blank=True, null=True)
    certificate = models.TextField(_('Сертификат'), null=True, blank=True)
    type = models.CharField(_('Тип'), choices=TypeFilmwork.choices, max_length=1)
    genres = models.ManyToManyField('Genre', through='GenreFilmwork')
    persons = models.ManyToManyField('Person', through='PersonFilmwork')
    rating = models.FloatField(_('Рейтинг'), blank=True, null=True, validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
    file_path = models.FileField(_('Файл'), blank=True, null=True, upload_to='movies/')

    class Meta:
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')
        db_table = "content\".\"film_work"

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"


class PersonFilmwork(UUIDMixin):
    class RoleType(models.TextChoices):
        ACTOR = 'A', _('Актер')
        WRITER = 'W', _('Сценарист')
        DIRECTOR = 'D', _('Директор')

    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.CharField(_('Роль'), null=True, max_length=1, choices=RoleType.choices)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"