# Generated by Django 3.1.7 on 2021-03-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('district', models.CharField(max_length=60)),
            ],
        ),
    ]
