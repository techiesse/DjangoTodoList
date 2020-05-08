from django.db import models

# Create your models here.

class Checklist(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)
    checked = models.BooleanField(default = False)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
