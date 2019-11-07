# Generated by Django 2.2.3 on 2019-11-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_computer_rawdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='score_buffer',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('routine_score', models.FloatField()),
                ('professional_score', models.FloatField()),
                ('price_score', models.FloatField()),
                ('enjoyment_score', models.FloatField()),
                ('year_score', models.FloatField()),
                ('battery_score', models.FloatField()),
                ('beauty_score', models.FloatField()),
                ('disk_score', models.FloatField()),
                ('processor_score', models.FloatField()),
                ('screen_score', models.FloatField()),
                ('size_score', models.FloatField()),
            ],
        ),
    ]
