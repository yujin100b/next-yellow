# Generated by Django 2.0.13 on 2020-04-06 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default=None, max_length=15, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
