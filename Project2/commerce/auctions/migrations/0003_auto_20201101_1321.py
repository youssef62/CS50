# Generated by Django 3.1.1 on 2020-11-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(related_name='listings_commented', to='auctions.Comment'),
        ),
    ]