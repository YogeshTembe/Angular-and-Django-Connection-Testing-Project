# Generated by Django 3.1.4 on 2020-12-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_delete_output'),
    ]

    operations = [
        migrations.CreateModel(
            name='outputplot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=256)),
                ('y', models.CharField(max_length=256)),
            ],
        ),
    ]
