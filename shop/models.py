from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):  # магический метод влияет на передачу в содержимого в функцию print
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    student_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):  # магический метод влияет на передачу в содержимого в функцию print
        # return self.title + ' ' + str(self.student_qty)
        return self.title
