from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=25, null=True)
    
    def __str__(self):
        return f"Marca: {self.title}\nAño: {self.year}\nColor: {self.color}"
    
    
class Publisher(models.Model):
    name = models.TextField(max_length=200)
    adress = models.TextField(max_length=200)
    
    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField()
    
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500)
    

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_day = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")
    
    def __str__(self) -> str:
        return  self.title
    