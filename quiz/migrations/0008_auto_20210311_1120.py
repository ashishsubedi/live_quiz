# Generated by Django 3.1.7 on 2021-03-11 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0007_auto_20210311_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreboard',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoreboard', to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='scoreboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoreboard', to=settings.AUTH_USER_MODEL),
        ),
    ]
