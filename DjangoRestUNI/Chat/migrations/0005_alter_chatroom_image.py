# Generated by Django 5.0.2 on 2024-02-16 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0004_chatroom_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='groups'),
        ),
    ]
