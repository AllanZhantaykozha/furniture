from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse


class Bigfurn(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='bigfurn_category')
    photo = models.ImageField(upload_to='bigturn_photo/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=150)
    contact = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('detail_bigfurn', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

    
class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title