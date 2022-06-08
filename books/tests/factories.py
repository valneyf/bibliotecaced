import factory
import factory.fuzzy

from ..models import Category, Book


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Category


class AuthorFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Author


class BookFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(CategoryFactory)
    name = factory.fuzzy.FuzzyText()
    image = factory.django.ImageField()
    published = factory.fuzzy.FuzzyDate(datetime.date(1500, 1, 1))
    pages = factory.fuzzy.FuzzyInteger(3000)
    is_available = factory.Faker("pybool")

    class Meta:
        model = Book
