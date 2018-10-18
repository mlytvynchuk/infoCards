from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=256,db_index=True)
    description = models.TextField(db_index=True)
    tags = models.ManyToManyField('Tag',blank=True,related_name='cards')
    slug = models.SlugField(max_length=150)
    image = models.ImageField(default='default.png',upload_to='cards_pics')


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)





