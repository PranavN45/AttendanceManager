# Generated by Django 4.1.7 on 2023-04-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_rename_cltrid_classteacher_classteacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classteacher',
            name='id',
        ),
        migrations.AlterField(
            model_name='classteacher',
            name='classTeacher_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
