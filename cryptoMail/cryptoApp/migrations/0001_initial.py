# Generated by Django 4.0.4 on 2022-05-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('destructionOption', models.IntegerField()),
                ('creationDate', models.DateField()),
                ('destructionDate', models.DateField()),
                ('password', models.CharField(max_length=50)),
                ('notificationEmail', models.EmailField(max_length=254)),
                ('sendEmail', models.BooleanField(default=False)),
                ('isDestroyed', models.BooleanField(default=False)),
                ('confirmation', models.BooleanField(default=False)),
            ],
        ),
    ]
