# Generated by Django 5.0.2 on 2024-02-22 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog Post!', max_length=250),
        ),
    ]
