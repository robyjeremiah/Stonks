# Generated by Django 2.2 on 2022-02-22 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stonks', '0002_auto_20220221_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=50, verbose_name='role'),
        ),
    ]
