# Generated by Django 2.2.12 on 2020-05-31 01:39

from django.db import migrations, models
import myApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_auto_20200521_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre_E', models.CharField(max_length=300)),
                ('Version_E', models.CharField(max_length=12)),
                ('Club_E', models.CharField(max_length=100)),
                ('Image_E', models.FileField(null=True, upload_to=myApp.models.upload_Image_path)),
            ],
        ),
    ]
