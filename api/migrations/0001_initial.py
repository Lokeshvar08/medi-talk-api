# Generated by Django 3.1.3 on 2020-11-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('specialisation', models.CharField(max_length=250)),
                ('hospital', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('application_rating', models.FloatField()),
                ('google_rating', models.FloatField()),
                ('article_rating', models.FloatField()),
                ('average_rating', models.FloatField()),
            ],
        ),
    ]
