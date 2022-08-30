# Generated by Django 4.1 on 2022-08-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_alter_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='The Father', max_length=40)),
                ('image', models.ImageField(upload_to='static/uploads')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
