# Generated by Django 3.1.1 on 2020-11-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_auto_20201103_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(related_name='listings_commented', to='auctions.Comment'),
        ),
    ]
