# Generated by Django 5.1.7 on 2025-03-09 18:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_html', models.TextField(blank=True, default='', editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GenreFellow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fellowships', to='genres.genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_genre', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('genre', 'user')},
            },
        ),
        migrations.AddField(
            model_name='genre',
            name='fellows',
            field=models.ManyToManyField(through='genres.GenreFellow', to=settings.AUTH_USER_MODEL),
        ),
    ]
