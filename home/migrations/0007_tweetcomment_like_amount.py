# Generated by Django 3.2.2 on 2021-06-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_tweet_tweet_like_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetcomment',
            name='like_amount',
            field=models.IntegerField(default=0),
        ),
    ]
