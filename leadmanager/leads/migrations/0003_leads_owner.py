# Generated by Django 3.0.6 on 2020-05-30 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0002_auto_20200530_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL),
        ),
    ]
