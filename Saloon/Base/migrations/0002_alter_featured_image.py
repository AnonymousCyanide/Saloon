# Generated by Django 4.1 on 2022-08-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='image',
            field=models.ImageField(upload_to='static/uploads'),
        ),
    ]