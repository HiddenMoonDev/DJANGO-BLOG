# Generated by Django 5.0.2 on 2024-03-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]