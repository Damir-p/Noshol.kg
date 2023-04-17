from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.core import validators


from apps.common.constants import UserType
from apps.common.models import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):
    
    # name = models.CharField()
    # email = models.EmailField()

    id = models.UUIDField(
        primary_key=True, 
        db_index=True, 
        default=uuid4
    )
    number = models.CharField(
        max_length=60, 
        # validators='', 
        verbose_name='Номер телефона'
    )
    type = models.CharField(
        max_length=20, 
        choices=UserType.choices,  
        default=UserType.CONSUMER ,  
        verbose_name="Тип пользователя"
    )
    # postgis
    geo = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="Геолокация"
    )
    rating = models.PositiveIntegerField(
        default=0, 
        blank=True, 
        null=True, 
        verbose_name="Рейтинг"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'


    def __str__(self):
     return f'{self.username} Тел: {self:number}'

    def clean(self):
        super().clean()
        if self.type == UserType.PRODUCER:
            if self.geo is None:
                raise validators.ValidationError(
                    'Ты находчик, у тебя обязательное поле геолокации'
                )
            if self.rating is None:
                raise validators.ValidationError(
                      'Ты находчик, у тебя обязательное поле рейтинга'
                )

# class Image(models.Model):
#     id = models.UUIDField()
#     image = models.FileDescriptor()
#     bitch = models.ForeignKey(Bitch, related_name=(image))
#     is_preview = models.BooleanField()

