# Generated by Django 4.2.5 on 2023-09-21 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='users.user'),
        ),
        migrations.AlterField(
            model_name='match',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='users.user'),
        ),
    ]
