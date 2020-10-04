from django.db import models

# Create your models here.
from user.models import User


class Post(models.Model):
    class META:
        managed = True;
        db_table = 'post'

    id = models.AutoField(primary_key=True);
    title = models.CharField(max_length=128, null=False);
    pubdate = models.DateField(null=False, auto_now=True);
    author = models.ForeignKey(User, on_delete=models.CASCADE);
    content = models.OneToOneField('Content', on_delete=models.CASCADE);

    def __repr__(self):
        return "POST {} {} {}".format(self.title, self.author.name, self.content.content[:10]);

    __str__ = __repr__


class Content(models.Model):
    class META:
        managed = True;
        db_table = 'content'

    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=40000, null=False);

    def __repr__(self):
        return "Content {} {}".format(self.id, self.content[:10])

    __str__ = __repr__
