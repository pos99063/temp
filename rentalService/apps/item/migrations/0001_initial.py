# Generated by Django 2.1.2 on 2018-11-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registDate', models.DateField(auto_now=True)),
                ('status', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
                ('minRentDay', models.IntegerField()),
                ('maxRentDay', models.IntegerField()),
                ('picture', models.ImageField(blank=True, max_length=128, upload_to='images/%Y/%m-%d')),
                ('info', models.TextField()),
            ],
        ),
    ]
