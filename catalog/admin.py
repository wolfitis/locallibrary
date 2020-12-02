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
	pass

# register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Now to create and register the new models; 
# for the purpose of this demonstration, we'll instead use the @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax):

# register the admin calsses for book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass

# register the admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	pass