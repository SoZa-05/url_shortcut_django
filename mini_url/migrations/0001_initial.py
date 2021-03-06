# Generated by Django 2.1.3 on 2018-12-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_long', models.URLField(unique=True)),
                ('code', models.IntegerField(unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('pseudo', models.CharField(max_length=100)),
                ('nbr_access', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
