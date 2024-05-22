from django.db import models
from string import ascii_letters,digits
from random import choice 
baselink = "http://127.0.0.1:8000/api/"
# Create your models here.
class ShortLink(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    def generate_short_url(self):
        length = 6
        characters = ascii_letters + digits
        short_url = baselink
        short_url = short_url+  ''.join(choice(characters) for _ in range(length))
        while ShortLink.objects.filter(short_url=short_url).exists():
            short_url = ''.join(choice(characters) for _ in range(length))
        return short_url
    
    def __str__(self) -> str:
        return f"{self.original_url}"