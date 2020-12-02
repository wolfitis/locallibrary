from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

# to customize the admin layout
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Inline editing of associated records
class BookInstanceInline(admin.TabularInline):
	model = BookInstance
	extra = 0

# Now to create and register the new models; 
# for the purpose of this demonstration, we'll instead use the @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax):

'''
We're showing you how because calling functions in your models can be very useful for other reasons — for example to add a Delete link next to every item in the list.
display_genre
'''
# register the admin calsses for book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BookInstanceInline]


# register the admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')

	# sectioning detail view
	fieldsets = (
		(None, {
			'fields': ('book', 'imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back')
		}),
	)

