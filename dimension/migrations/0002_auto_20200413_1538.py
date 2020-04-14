# Generated by Django 3.0.1 on 2020-04-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimension', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dim',
            name='image_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dim',
            name='image_width',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dim',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to='documents/', width_field='image_width'),
        ),
    ]