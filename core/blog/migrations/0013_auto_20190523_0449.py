# Generated by Django 2.2 on 2019-05-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190505_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['add_time']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['add_time']},
        ),
        migrations.AddField(
            model_name='comment',
            name='moderation',
            field=models.BooleanField(default=False),
        ),
    ]
