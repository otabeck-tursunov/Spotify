# Generated by Django 5.0.4 on 2024-04-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albom',
            name='rasm',
            field=models.ImageField(blank=True, null=True, upload_to='albomlar/'),
        ),
        migrations.AlterField(
            model_name='qoshiq',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='qoshiqlar/'),
        ),
        migrations.AlterField(
            model_name='qoshiq',
            name='davomiylik',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qoshiqchi',
            name='t_sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]
