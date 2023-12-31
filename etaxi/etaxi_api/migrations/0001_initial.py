# Generated by Django 4.2.7 on 2023-11-04 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('quote', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='etaxi_api.city')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='etaxi_api.city')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='etaxi_api.city')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=64)),
                ('transmission', models.CharField(max_length=64)),
                ('engine_capacity', models.CharField(max_length=64)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='etaxi_api.city')),
            ],
        ),
    ]
