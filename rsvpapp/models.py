from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class RSVP(models.Model):
    RSVP_CHOICES = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default="yemi.oa@gmail.com", max_length=50)
    will_be_present = models.CharField(max_length=10, choices=RSVP_CHOICES, default='YES')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' --- ' + self.will_be_present+ '\r\n' + self.email

    def get_absolute_url(self):
        return reverse('create_rsvp')

    class Meta:
        ordering = ['first_name']