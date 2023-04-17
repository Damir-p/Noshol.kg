from django.db import models
from uuid import uuid4


from apps.common.models import AbstractBaseModel


class Category(AbstractBaseModel):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid4)
    name = models.CharField(max_length=120, verbose_name="Название")
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='children',
        verbose_name="Родительская категория"
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class Bitch(AbstractBaseModel):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid4)
    
    # title = models.CharField()
    # description = models.TextField()
    # image = models.CharField()
    # price = models.DecimalField()
    # author = models.ForeignKey()
    # category = models.ForeignKey()
