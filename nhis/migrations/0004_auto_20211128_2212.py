# Generated by Django 3.2.9 on 2021-11-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhis', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='DisaCtr',
        ),
        migrations.DeleteModel(
            name='PragCtr',
        ),
    ]
