# Generated by Django 4.0.6 on 2022-07-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
