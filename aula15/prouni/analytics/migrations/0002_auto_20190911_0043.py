# Generated by Django 2.2.5 on 2019-09-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ufcampus',
            name='uf',
            field=models.TextField(choices=[(1, 'RS'), (2, 'SC'), (3, 'PR')], max_length=2),
        ),
    ]