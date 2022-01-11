from django.db import models

class book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    pages = models.IntegerField(default=1)
    cover = models.ImageField(default='default.jpg',upload_to="book")

    def __str__(self) -> str:
        return self.name