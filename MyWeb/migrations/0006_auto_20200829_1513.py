# Generated by Django 3.1 on 2020-08-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0005_abilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='abilities',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
