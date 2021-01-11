from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
# Uses an Object-Relational Mapper (ORM). Similar to a SQL database, but without having to learn another language
# Creates database in SQLite format by default (Can use others as well)

fs = FileSystemStorage(location='projects/static')

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(storage=fs)
    def __str__(self):
        return 'Project: {}'.format(self.title)