# Generated by Django 3.1.1 on 2020-11-02 12:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20201102_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ManyToManyField(null=True, related_name='bids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(related_name='comments_posted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(related_name='listings_commented', to='auctions.Comment'),
        ),
    ]
