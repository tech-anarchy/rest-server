# Generated by Django 5.0.2 on 2024-02-27 05:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqua', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsrData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammonia', models.FloatField(blank=True, default=None, null=True)),
                ('phosphate', models.FloatField(blank=True, default=None, null=True)),
                ('calcium', models.IntegerField(blank=True, default=None, null=True)),
                ('magnesium', models.IntegerField(blank=True, default=None, null=True)),
                ('ph', models.FloatField(blank=True, default=None, null=True)),
                ('dkh', models.FloatField(blank=True, default=None, null=True)),
                ('temparature', models.FloatField(blank=True, default=None, null=True)),
                ('nitrate', models.FloatField(blank=True, default=None, null=True)),
                ('nitrite', models.FloatField(blank=True, default=None, null=True)),
                ('salinity', models.FloatField(blank=True, default=None, null=True)),
                ('b_filterCarbon', models.BooleanField(blank=True, default=False, null=True)),
                ('b_filterAmmonia', models.BooleanField(blank=True, default=False, null=True)),
                ('b_filterPhosphate', models.BooleanField(blank=True, default=False, null=True)),
                ('b_filterSponges', models.BooleanField(blank=True, default=False, null=True)),
                ('water_change', models.IntegerField(blank=True, default=None, null=True)),
                ('dose', models.CharField(blank=True, choices=[('F1', 'FUSION1'), ('F2', 'FUSION2'), ('AM', 'AMINO'), ('MD', 'MED'), ('OT', 'OTHER')], default=None, max_length=2, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('time', models.TimeField(auto_now=True)),
                ('tank', models.ForeignKey(db_column='tank', on_delete=django.db.models.deletion.CASCADE, to='aqua.tank', to_field='uuid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
