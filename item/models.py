from django.contrib.auth.models import User
from mysite.utils import uuid_upload_to
from django.db import models
from django.urls import reverse

class Maker(models.Model):
    name = models.CharField(max_length=200, verbose_name='이름')
    phone = models.CharField(max_length=200, verbose_name='전화번호')
    address = models.CharField(max_length=800, verbose_name='주소')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_maker', args=[self.pk])

class Mate(models.Model):
    name = models.CharField(max_length=200, verbose_name='제품명')
    desc = models.TextField(verbose_name='제품 설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    leftover = models.PositiveIntegerField(verbose_name='남은 수량')
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to, verbose_name='제품 사진')
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, verbose_name='거래처', related_name='products')

    def get_absolute_url(self):
        return reverse('detail_item', args=[self.pk])


