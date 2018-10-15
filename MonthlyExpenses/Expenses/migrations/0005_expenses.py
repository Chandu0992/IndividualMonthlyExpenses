# Generated by Django 2.1.2 on 2018-10-09 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Expenses', '0004_auto_20181010_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Expenses.Register')),
            ],
        ),
    ]