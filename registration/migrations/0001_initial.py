# Generated by Django 5.0.6 on 2024-05-08 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('mobno', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
