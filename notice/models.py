from django.db import models

from users.models import User


class Ads(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название товара",
                             help_text="Введите название товара")
    price = models.IntegerField(verbose_name="цена товара",
                                help_text="Введите цену товара (целое число)")
    description = models.TextField(verbose_name="описание товара",
                                   help_text="Введите описание товара",
                                   null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Создатель",
                               related_name="user_habit")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="время и дата создания объявления")

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"
        ordering = ['created_at']


class Comment(models.Model):
    text = models.TextField(verbose_name="текст отзыва",
                            help_text="Введите текст отзыва")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Создатель",
                               related_name="user_comment")
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE,
                           verbose_name="Создатель",
                           related_name="notice_commit")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="время и дата создания объявления")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['created_at']
