from django.db import models


class Author(models.Model):
    """Model for an author"""
    author_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
