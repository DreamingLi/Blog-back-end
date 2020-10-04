# Create your models here.

from django.db import models


class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=60, null=False);
    email = models.CharField(max_length=60, null=False);
    password = models.CharField(max_length=60, null=False);

    def __repr__(self):
        return "USER : {} {} {}".format(self.id, self.name, self.email)

    __str__ = __repr__
