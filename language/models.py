from django.db import models
from froala_editor.fields import FroalaField
from ckeditor.fields import RichTextField
# Create your models here.


class Language(models.Model):
    """Model definition for Language."""

    # TODO: Define fields here
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    description = RichTextField(max_length=200, default="")

    class Meta:
        """Meta definition for Language."""
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        '''just returns name in the admin '''
        return self.name
