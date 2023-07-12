# Generated by Django 4.2.3 on 2023-07-12 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('command', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Finished', 'Finished')], max_length=255)),
                ('parameters', models.CharField(max_length=255)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='docker_app.app')),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentVariable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='envs', to='docker_app.app')),
            ],
        ),
    ]