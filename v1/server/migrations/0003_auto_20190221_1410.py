# Generated by Django 2.1.5 on 2019-02-21 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20190114_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='server.Order'),
        ),
    ]
