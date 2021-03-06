# Generated by Django 3.1.1 on 2020-11-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20201102_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(related_name='listings_commented', to='auctions.Comment'),
        ),
    ]
