# Generated by Django 5.2.2 on 2025-06-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0003_alter_birthday_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='image',
            field=models.ImageField(blank=True, upload_to='birthdays_images', verbose_name='Фото'),
        ),
    ]
