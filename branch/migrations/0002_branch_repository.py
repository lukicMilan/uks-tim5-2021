# Generated by Django 3.2.11 on 2022-01-24 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository'),
        ),
    ]
