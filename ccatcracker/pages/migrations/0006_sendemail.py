# Generated by Django 2.2.1 on 2019-08-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_aptitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=111, unique=True)),
                ('status', models.CharField(default='New', max_length=111)),
                ('msaterial', models.CharField(default='No', max_length=111)),
            ],
        ),
    ]
