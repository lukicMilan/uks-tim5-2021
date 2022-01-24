# Generated by Django 3.2.11 on 2022-01-24 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('is_default', models.BooleanField(default=False)),
                ('is_base_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.branch')),
            ],
        ),
    ]
