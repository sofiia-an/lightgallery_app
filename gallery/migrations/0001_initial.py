# Generated by Django 3.1 on 2020-08-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtitle', models.CharField(max_length=100)),
                ('imgdesc', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
