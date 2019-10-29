from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    phone_id = models.DecimalField(max_digits=10,decimal_places=2,primary_key=True)
    phone_name = models.CharField(max_length=50, default='')
    phone_link = models.CharField(max_length=50)
    phone_price = models.DecimalField(max_digits=10,decimal_places=2)
    phone_data = models.DateTimeField(auto_now=False, null=True, blank=True)
    phone_n_slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.phone_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.phone_name)
        super(Phone, self).save(*args, **kwargs)
