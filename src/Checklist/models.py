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


    def remove_item(self, item):
        item = self._get_item(item)
        item.delete()


    def check_item(self, item, checked = True):
        item = self._get_item(item)
        item.checked = checked
        item.save()


    def _get_item(self, item):
        assert isinstance(item, int) or isinstance(item, Item)
        item_id = item if isinstance(item, int) else item.id
        item = self.item_set.get(id=item_id)
        return item


    def get_item(self, item_id):
        item = self.item_set.get(id=item_id)
        return item


class Item(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)
    checked = models.BooleanField(default = False)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)


    def __str__(self):
        return f'({self.id}) {self.name}'
