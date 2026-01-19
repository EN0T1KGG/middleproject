from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    # Кастомная модель пользователя
    email = models.EmailField(unique=True,null=False)
    description = models.TextField()
    phone = models.CharField(max_length=11, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/')
    image = models.URLField()
    groups = models.ManyToManyField(
            'auth.Group',
            related_name='custom_user',
            blank=True
    )

    def __str__(self):
        return self.username        