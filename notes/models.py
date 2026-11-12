from django.db import models


class Note(models.Model):
    title = models.CharField('Sözbaşy', max_length=120)
    text = models.TextField('Mazmuny', blank=True)
    done = models.BooleanField('Ýerine ýetirildi', default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
