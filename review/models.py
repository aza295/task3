from django.contrib.auth.models import User
from django.db import models
from product.models import Product

RAITING =[
    (1,'AWFUL'),
    (2,'POOR'),
    (3,'AVERAGE'),
    (4,'GOOD'),
    (5,'EXCELLENT')
]


class Review(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    text = models.TextField('Текст')
    raiting = models.IntegerField(choices=RAITING)

    class Meta:
        verbose_name_plural = 'Оценка'

    def __str__(self):
        return self.text


