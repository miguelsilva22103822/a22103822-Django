# Generated by Django 4.2.1 on 2023-06-08 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_author_areas_author_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='like_post', to='portfolio.post'),
        ),
    ]
