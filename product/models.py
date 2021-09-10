from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(primary_key=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField('Title',max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,
                             on_delete=models.CASCADE,
                             )

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title





