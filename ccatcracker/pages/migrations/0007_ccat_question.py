# Generated by Django 2.2.1 on 2019-08-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_sendemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCAT_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField()),
                ('question', models.TextField(blank=True)),
                ('ans', models.TextField(blank=True)),
                ('a', models.CharField(blank=True, max_length=20)),
                ('b', models.CharField(blank=True, max_length=20)),
                ('c', models.CharField(blank=True, max_length=20)),
                ('d', models.CharField(blank=True, max_length=20)),
                ('display', models.TextField(blank=True, default='Yes')),
            ],
        ),
    ]
