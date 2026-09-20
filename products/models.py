from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='styles')

    def __str__(self):
        return self.name

class Product(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='products')
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.style.name