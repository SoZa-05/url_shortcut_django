from django.db import models


# Create your models here.


class MiniUrl(models.Model):
    url_long = models.URLField(unique=True)
    code = models.IntegerField(unique=True)
    created_at = models.DateField(auto_now_add=True)
    pseudo = models.CharField(max_length=100)
    nbr_access = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.url_long
