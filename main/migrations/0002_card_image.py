# Generated by Django 3.1.6 on 2021-05-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]
