from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User


class PostClass(models.Model):
    # objects = None
    title = models.CharField(max_length=255, verbose_name="Заголовок")  # максимальна довжина заголовку 255 символів
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")  # unique=True це унакальна url-адреса
    content = models.TextField(blank=False, verbose_name="Текст")  # поле не може бути порожнім
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Зображення")  # завантажується до
    document = models.FileField(blank=True, upload_to="documents/%Y/%m/%d/", verbose_name="Додаток")  # завантажуэться до
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Змінено")
    is_published = models.BooleanField(default=True, verbose_name="Публікація")
    cat = models.ForeignKey('CategoryClass', on_delete=models.PROTECT, verbose_name="Категорія")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post', kwargs={'post_slug': self.slug})
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Допис головного додатку'
        verbose_name_plural = 'Дописи головного додатку'
        ordering = ['-time_create', 'title']


class CategoryClass(models.Model):
    # objects = None
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорія")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")  # unique=True це унакальна url-адреса

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id']


TIME_CHOICES = (
    ("15:00", "15:00"),
)


class BookingHouseClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    holidayhouse = models.ForeignKey('HolidayHouse', on_delete=models.PROTECT, verbose_name='Будинок відпочинку')
    day = models.DateField(default=datetime.now)
    booking_pets = models.TextField(max_length=255, blank=True, verbose_name='Домашні улюбленці')
    booking_wish = models.TextField(max_length=255, blank=True, verbose_name='Додаткові послуги')  # will need to be rename
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="15:00")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    # price = models.IntegerField(default=5000)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

    class Meta:
        verbose_name = 'Бронювання будинку відпочинку'
        verbose_name_plural = 'Бронювання будинків відпочинку'
        ordering = ['id']


class HolidayHouse(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Будинок відпочинку')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Будинок відпочинку'
        verbose_name_plural = 'Будинок відпочинку'
        ordering = ['id']
