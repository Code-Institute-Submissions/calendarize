# Generated by Django 2.2.7 on 2019-11-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20191122_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(default='a.jpg', upload_to='media/'),
        ),
    ]