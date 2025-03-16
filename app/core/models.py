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
