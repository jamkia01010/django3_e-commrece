# Generated by Django 4.1 on 2022-09-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_proflie_active_alter_proflie_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="numbers",
            name="phone_num",
            field=models.CharField(max_length=15),
        ),
    ]
