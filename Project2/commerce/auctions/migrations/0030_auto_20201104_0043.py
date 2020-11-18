# Generated by Django 3.1.1 on 2020-11-03 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_auto_20201104_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_posted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(related_name='listings_commented', to='auctions.Comment'),
        ),
    ]