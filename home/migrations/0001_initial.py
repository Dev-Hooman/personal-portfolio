# Generated by Django 4.0.4 on 2022-06-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=13)),
                ('email', models.CharField(max_length=150)),
                ('content', models.TextField()),
            ],
        ),
    ]
