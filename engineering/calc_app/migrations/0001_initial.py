# Generated by Django 2.2.2 on 2019-07-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rectangle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_width', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rec_height', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
