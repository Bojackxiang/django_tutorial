from django.db import models

# Create your models here.
class Language(models.Model):
    """Model definition for Language."""

    # TODO: Define fields here
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)

    class Meta:
        """Meta definition for Language."""

        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        '''just returns name in the admin '''
        return self.name

