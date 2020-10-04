# Generated by Django 3.1 on 2020-08-29 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]