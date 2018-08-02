# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easypr_general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=175)),
                ('title_slug', models.CharField(max_length=200)),
                ('post_body', models.TextField(blank=True, max_length=3000, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[(b'top-blogs', b'Top Blogs'), (b'technology', b'Technology')], max_length=75)),
                ('active', models.BooleanField(default=True)),
                ('tags', models.CharField(max_length=500)),
                ('post_image', models.ImageField(upload_to=b'blogpost_images')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
