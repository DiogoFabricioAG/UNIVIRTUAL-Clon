# Generated by Django 5.0.2 on 2024-02-09 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_blogpost_attachment_file_alter_blogpost_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='likes', to='Blog.blogpost'),
        ),
    ]
