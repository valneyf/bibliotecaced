from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category, Book


class BookDetailView(DetailView):
    queryset = Book.available.all()


class BookListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Book.available.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ('name', 'category', 'author', 'published', 'pages', 'image')


class BookUpdateView(UpdateView):
    model = Book
    fields = ('name', 'category', 'author', 'published', 'pages', 'image')
    template_name_suffix = '_update_form'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('list')
