from django.db import models

class Diary(models.Model):
    text=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return 'Diary  {}'.format(self.id)
    class Meta:
        verbose_name_plural='Diary'

