# Generated by Django 2.1 on 2018-11-09 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20181109_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodytext', models.TextField(verbose_name='message')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', verbose_name='ip address')),
                ('user_name', models.CharField(default='anonymous', max_length=50, verbose_name='user name')),
                ('user_email', models.EmailField(blank=True, max_length=254, verbose_name='user email')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['post_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('uploadedImage', models.ImageField(db_column='Upload an Image', upload_to='Uploads/%Y/%m/')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField()),
                ('bodytext', models.TextField(verbose_name='message')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('modified', models.DateTimeField(null=True, verbose_name='modified')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('comment_count', models.IntegerField(blank=True, default=0, verbose_name='comment count')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='posted by')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-post_date'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
