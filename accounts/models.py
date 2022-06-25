from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # email only allow mail.bnu.edu.cn or bnu.edu.cn
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        },
    )
    pass

