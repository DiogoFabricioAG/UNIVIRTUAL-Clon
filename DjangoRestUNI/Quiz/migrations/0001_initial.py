# Generated by Django 5.0.2 on 2024-02-11 04:46

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0009_coursematerial_is_visible'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qualification', models.IntegerField()),
                ('problems', models.IntegerField()),
                ('typeof', models.CharField(choices=[('Quick (NON Q)', 'Quick (NON Q)'), ('Practice (PC)', 'Practice (PC)'), ('Parcial (EP)', 'Parcial (EP)'), ('Final (EF)', 'Final (EF)'), ('Sustitutorio (ES)', 'Sustitutorio (ES)')], default='Quick (NON Q)', max_length=20)),
                ('time', models.DurationField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='Course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('solutions', models.IntegerField(default=4)),
                ('points', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='ProblemImage')),
                ('quiz', models.ManyToManyField(related_name='quizproblems', to='Quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ProblemImage')),
                ('problem', models.ManyToManyField(related_name='problem_solutions', to='Quiz.quizproblem')),
            ],
        ),
    ]
