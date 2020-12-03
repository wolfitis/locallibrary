from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookInstance.as_view(), name='books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
