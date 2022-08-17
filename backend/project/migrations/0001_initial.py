# Generated by Django 3.2.15 on 2022-08-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('repository', models.URLField(max_length=128)),
                ('users', models.ManyToManyField(to='user.User')),
            ],
        ),
    ]