# Generated by Django 4.1.7 on 2023-03-02 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('orders', '0002_rename_orderedproduct_orderedproductmodel_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserModel',
        ),
    ]
