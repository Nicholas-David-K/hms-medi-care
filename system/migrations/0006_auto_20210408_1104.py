# Generated by Django 3.1.7 on 2021-04-08 08:04

from django.db import migrations, models
import django.db.models.deletion
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_remove_appointment_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', encrypted_fields.fields.EncryptedCharField(max_length=200)),
                ('diagnosis', encrypted_fields.fields.EncryptedCharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.prescription'),
        ),
    ]
