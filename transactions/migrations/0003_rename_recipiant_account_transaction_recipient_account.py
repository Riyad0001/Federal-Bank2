# Generated by Django 4.0.10 on 2024-12-04 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_recipiant_account_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='recipiant_account',
            new_name='recipient_account',
        ),
    ]
