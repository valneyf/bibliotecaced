# Generated by Django 4.0.5 on 2022-06-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(),
        ),
    ]
