from django.db import models
import datetime as dt

class Image(models.Model):
    image = models.ImageField(upload_to = 'photo/')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def photo_details(cls):
        today = dt.date.today()
        photo = cls.objects.all()
        return photo

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
