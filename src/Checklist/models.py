from django.db import models

# Create your models here.

class Checklist(models.Model):
    name = models.CharField(max_length = 50)


    def __str__(self):
        return f'{self.name}({self.id})'


    def add_item(self, name, description, checked = False):
        item = Item.objects.create(
            name =  name,
            description = description,
            checked = checked,
            checklist = self,
        )
        
        return item


class Item(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)
    checked = models.BooleanField(default = False)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
