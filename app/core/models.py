from django.db import models


class Author(models.Model):
    """Model for an author"""
    author_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model for a book"""
    book_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(
        Author,
        related_name='authors',
        related_query_name='Author.name')

    def __str__(self):
        return self.name


class User(models.Model):
    """Model for a user"""
    user_id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
