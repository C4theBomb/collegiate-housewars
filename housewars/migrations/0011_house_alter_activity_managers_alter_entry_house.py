# Generated by Django 4.0.4 on 2022-05-18 22:10

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('housewars', '0010_remove_activity_session1_signups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelManagers(
            name='activity',
            managers=[
                ('session1', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housewars.house'),
        ),
    ]
