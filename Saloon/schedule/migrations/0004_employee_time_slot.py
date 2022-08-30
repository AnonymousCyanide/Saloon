# Generated by Django 4.1 on 2022-08-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_remove_customer_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='time_slot',
            field=models.JSONField(default='[[0, "09:00 \\u2013 09:30"], [1, "10:00 \\u2013 10:30"], [2, "11:00 \\u2013 11:30"], [3, "12:00 \\u2013 12:30"], [4, "13:00 \\u2013 13:30"], [5, "14:00 \\u2013 14:30"], [6, "15:00 \\u2013 15:30"], [7, "16:00 \\u2013 16:30"], [8, "17:00 \\u2013 17:30"]]'),
        ),
    ]