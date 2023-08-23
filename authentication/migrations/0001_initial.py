# Generated by Django 4.2.4 on 2023-08-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(default=None, max_length=100, unique=True)),
                ('password', models.CharField(default=None, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('role', models.IntegerField(choices=[(0, 'staff'), (1, 'restauranter')], default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]