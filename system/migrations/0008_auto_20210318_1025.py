# Generated by Django 3.1.7 on 2021-03-18 07:25

from django.db import migrations, models
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20210318_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=encrypted_fields.fields.EncryptedCharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
    ]
