# Generated by Django 3.0.6 on 2020-11-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='targetArea',
            field=models.CharField(default='-', max_length=400),
            preserve_default=False,
        ),
    ]
