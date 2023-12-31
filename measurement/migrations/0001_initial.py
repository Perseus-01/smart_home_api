# Generated by Django 4.2.4 on 2023-08-02 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(default=None, null=True, upload_to='')),
                ('sensor_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor')),
            ],
        ),
    ]
