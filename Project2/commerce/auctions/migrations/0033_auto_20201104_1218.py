# Generated by Django 3.1.1 on 2020-11-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_auto_20201104_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(related_name='listings_commented', to='auctions.Comment'),
        ),
    ]
