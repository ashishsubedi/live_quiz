# Generated by Django 3.1.7 on 2021-03-10 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_option_problem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='options',
        ),
        migrations.AddField(
            model_name='option',
            name='problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option', to='users.problem'),
        ),
    ]
