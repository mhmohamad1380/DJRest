# Generated by Django 3.2.7 on 2021-10-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
