# Generated by Django 2.1.2 on 2018-10-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenses', '0007_auto_20181011_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='dt',
            field=models.DateField(default=10, max_length=10),
        ),
    ]