from django.db import models

# Create your models here.
class Files_Db(models.Model):
    create_date = models.DateTimeField('creation date')
    name = models.CharField(max_length=128)
    path = models.CharField(max_length=128)
    size = models.IntegerField(default=0)
