# Generated by Django 3.0.1 on 2020-04-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimension', '0005_auto_20200414_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
