# Generated by Django 4.2.2 on 2023-07-06 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_pessoa_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='subject_teaching',
        ),
        migrations.AddField(
            model_name='person',
            name='subject_teaching',
            field=models.ManyToManyField(to='portfolio.subject'),
        ),
    ]
