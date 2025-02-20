# Generated by Django 3.2.16 on 2023-04-13 13:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', ckeditor.fields.RichTextField()),
                ('location', models.CharField(max_length=300)),
                ('job_type', models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=1)),
                ('salary', models.CharField(blank=True, max_length=30)),
                ('company_name', models.CharField(max_length=300)),
                ('company_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('url', models.URLField()),
                ('last_date', models.DateField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('Vacancy', models.CharField(max_length=10, null=True)),
                ('Experience', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('passedout', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='jobapp.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookmarkJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
