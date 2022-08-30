# Generated by Django 4.1 on 2022-08-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('heading', models.CharField(default='THE BEACON TO ALL MANKIND', max_length=40)),
                ('quote', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]