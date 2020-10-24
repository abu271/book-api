from django.core.management import call_command
from django.test import TestCase
from os import path
from core import models


_path = path.abspath(path.curdir)
csv_file_path = path.join(_path, 'core/tests/', 'test.csv')


class CommandTests(TestCase):
    def test_import_authors_via_csv_file(self):
        """
        Test import_authors command on test.csv file
        """
        call_command('import_authors', csv_file=csv_file_path)

        authors = models.Author.objects.all()

        self.assertEqual(len(authors), 5)

        # check first and last author names
        first_author = str(authors[0])
        last_author = str(authors[4])
        self.assertEqual(first_author, 'Edith Perry')
        self.assertEqual(last_author, 'Paige Moore')
