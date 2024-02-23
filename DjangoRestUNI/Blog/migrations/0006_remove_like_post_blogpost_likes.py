# Generated by Django 5.0.2 on 2024-02-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_remove_blogpost_likes_like_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='posts', to='Blog.like'),
        ),
    ]
