# Generated by Django 4.1 on 2022-08-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
