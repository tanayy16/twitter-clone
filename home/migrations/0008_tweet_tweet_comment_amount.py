# Generated by Django 3.2.2 on 2021-06-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_tweetcomment_like_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_comment_amount',
            field=models.IntegerField(default=0),
        ),
    ]
