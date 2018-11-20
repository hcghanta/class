from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('events:event_list_by_category',
                        args=[self.slug])


class Event(models.Model):
    category = models.ForeignKey(Category,
                                related_name='events',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    organisers = models.CharField(max_length=200, db_index=True)
    registration_deadline = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='events/%Y/%m/%d',
                                blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200, db_index=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:event_detail',
                       args=[self.id, self.slug])

