# Generated by Django 3.2.11 on 2022-01-24 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('milestone', '0001_initial'),
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='milestones',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestone.milestone'),
        ),
    ]
