from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return 'Category: {}'.format(self.name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # Timestamp updated when a row is first added to the database
    last_modified = models.DateTimeField(auto_now=True) # Timestamp updated every time an object is saved
    categories = models.ManyToManyField("Category", related_name='posts') # Allows many categories to be assigned to many posts
    def __str__(self):
        return 'Post: {}'.format(self.title)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE) # Similar to ManyToMany but now defines ManyToOne (many comments to one post)
    def __str__(self):
        return '{} on {}'.format(self.author, self.post)