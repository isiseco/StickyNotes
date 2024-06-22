from django.test import TestCase

# Create your tests here.
from .models import Note, Bulletin

class NoteModelTest(TestCase):

    def setUp(self):
        Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_content(self):
        note = Note.objects.get(id=1)
        expected_object_name = f'{note.title}'
        self.assertEqual(expected_object_name, 'Test Note')

class BulletinModelTest(TestCase):

    def setUp(self):
        Bulletin.objects.create(title="Test Bulletin", content="This is a test bulletin.")

    def test_bulletin_content(self):
        bulletin = Bulletin.objects.get(id=1)
        expected_object_name = f'{bulletin.title}'
        self.assertEqual(expected_object_name, 'Test Bulletin')