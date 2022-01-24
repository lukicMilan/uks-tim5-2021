# Generated by Django 3.2.11 on 2022-01-24 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=60)),
                ('website', models.CharField(max_length=60)),
                ('role', models.CharField(choices=[('Administrator', 'Administrator'), ('Authenticate user', 'Authenticate user'), ('Unauthenticate user', 'Unauthenticate user')], default='Unauthenticate user', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
