# Generated by Django 4.0.3 on 2022-05-26 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('can_mark_returned', 'Set book as returned'),),
            },
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('profile_picture', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('cohort', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pollmembers.cohort')),
            ],
        ),
    ]