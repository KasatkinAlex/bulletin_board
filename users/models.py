from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_USER = [
        ("user", "user"),
        ("admin", "admin")
    ]

    username = None

    first_name = models.CharField(max_length=200, verbose_name="Имя",
                                  help_text="Введите Ваше имя",
                                  null=True, blank=True)
    last_name = models.CharField(max_length=200, verbose_name="Фамилия",
                                 help_text="Введите Вашу фамилию",
                                 null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar_user/', verbose_name='аватар',
                               help_text='загрузите Ваше фото',
                               null=True, blank=True, )
    phone = models.CharField(max_length=30,
                             verbose_name='телефон',
                             null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True,
                              verbose_name='почта')
    role = models.CharField(default="user", choices=ROLE_USER,
                            verbose_name="роль пользователя, "
                                         "доступные значения: user, admin")
    token = models.CharField(max_length=200, verbose_name='Token',
                             blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
