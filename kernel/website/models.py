from django.db import models

# Create your models here.
class PreRegisterDriver(models.Model):
    """Model definition for PreRegisterDriver."""

    name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    email = models.CharField(max_length = 64, unique = True)
    phone_number = models.CharField(max_length = 11, unique = True)

    origin = models.CharField(max_length = 64)
    destination = models.CharField(max_length = 64)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for PreRegisterDriver."""
        verbose_name = 'پیش ثبت نام کاربر'
        verbose_name_plural = 'پیش ثبت نام کاربران'

    def __str__(self):
        """Unicode representation of PreRegisterDriver."""
        return '{} {}'.format(self.name, self.last_name)

