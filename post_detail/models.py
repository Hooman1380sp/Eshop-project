from cloudinary.models import CloudinaryField
from django.db import models
from django.utils.text import slugify

from accounts.models import User


class Category(models.Model):
    cat = models.CharField(max_length=100, null=True)
    parent = models.ManyToManyField('Category', blank=True)
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return self.cat


class Information(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    pre_price = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    descriotions = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True)
    is_delete = models.BooleanField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if Information.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.name + '-' + str(self.id))
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class ProductVisit(models.Model):
    product = models.ForeignKey('Information', on_delete=models.CASCADE)
    ip = models.CharField(max_length=30)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} / {self.ip}'
