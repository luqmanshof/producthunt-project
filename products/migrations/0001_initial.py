# Generated by Django 2.2.4 on 2019-08-28 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('url', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('votes_total', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='images/')),
                ('icon', models.ImageField(upload_to='images/')),
                ('body', models.TextField(max_length=500)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
