from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False,
                         populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:list_by_category", kwargs={"slug": self.slug})


class Author(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Book(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="books", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(unique=True, always_update=False,
                         populate_from="name")
    image = models.ImageField(upload_to="books/%Y/%m/%d", blank=True)
    published = models.DateField()
    pages = models.IntegerField()
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"slug": self.slug})
