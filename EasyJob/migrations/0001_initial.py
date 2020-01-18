# Generated by Django 2.2.7 on 2019-11-25 16:08

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=250)),
                ('compagny', models.CharField(max_length=100)),
                ('localisation', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('pubdate', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('diplome', models.CharField(max_length=255)),
                ('specialite', models.CharField(max_length=255)),
                ('Telephone', models.IntegerField()),
                ('competence', models.CharField(max_length=100)),
                ('localisation', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Favoris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.IntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyJob.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyJob.Utilisateur')),
            ],
        ),
    ]