# Generated by Django 2.0.13 on 2020-04-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextyellow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.CharField(default=None, max_length=15, null=True)),
            ],
        ),
    ]
