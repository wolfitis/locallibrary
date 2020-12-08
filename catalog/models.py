from django.db import models
from django.urls import reverse #to generate urls by reversing the url pattern
import uuid


# Create your models here.

# Genre model
class Genre(models.Model):
	name = models.CharField(max_length=50, help_text='Enter book\'s genere')
	
	# to return human-readable form of object
	def __str__(self):
		return self.name


# Book model in general, what books are available in out library
class Book(models.Model):
	title = models.CharField(max_length=120)
	author = models.ForeignKey('Author', on_delete = models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

	# many-to-many field because a book can have many generes and multiple books can be of same genere
	genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

	def display_genre(self):
		"""Create a string for the Genre. This is required to display genre in Admin."""
		return ', '.join(genre.name for genre in self.genre.all()[:3])	
	
	display_genre.short_description = 'Genre'

	
# BookInstance model, to carry details about individual book e.g. availablity, no. of copies etc
class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this book across whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=120)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintainance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Book availability',
	)

	class Meta:
		ordering = ['due_back']

	def __str__(self):
			return f'{self.id} ({self.book.title})'


# Author model
class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
			return f'{self.last_name}, {self.first_name}'

	class Meta:
		ordering = ['last_name']