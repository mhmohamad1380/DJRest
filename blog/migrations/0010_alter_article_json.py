# Generated by Django 3.2.7 on 2021-10-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='json',
            field=models.JSONField(blank=True, default='history', null=True),
        ),
    ]
