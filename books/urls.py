from django.urls import path

from .views import BookDetailView, BookListView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<slug:slug>/', BookDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', BookListView.as_view(), name='list_by_category')
]
