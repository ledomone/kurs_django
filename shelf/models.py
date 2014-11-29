from __future__ import unicode_literals, absolute_import
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Author(models.Model):
    # first_name = models.CharField(verbose_name=_("first name"), max_length=20)    # gTranslator,
    # first_name = models.CharField(_("first name"), max_length=20)    # gTranslator,
    first_name = models.CharField(verbose_name="Imię", max_length=20)
    last_name = models.CharField(_("last name"), max_length=50)

    class Meta:
        ordering = ("last_name", "first_name")
        verbose_name = _("Author")  # nie mianownik, tylko dopełniacz
        verbose_name_plural = _("Authors")

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name,
                                                 last_name=self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=70)
    url = models.CharField(max_length=250, default="http://www.")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class BookEdition(models.Model):
    book = models.ForeignKey(Book)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book,
                                                      publisher=self.publisher)


COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard')
    # wartość w bazie, wyświetlana nazwa
)


class BookItem(models.Model):
    edition = models.ForeignKey(BookEdition)
    cover = models.CharField(max_length=4, choices=COVER_TYPES)  # rodzaj okładki

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition,
                                           cover=self.get_cover_display())
