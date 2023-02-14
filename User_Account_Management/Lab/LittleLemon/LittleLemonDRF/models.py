from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem_id =  models.SmallIntegerField()
    rating = models.SmallIntegerField()


    def __str__(self) -> str:
        return self.user