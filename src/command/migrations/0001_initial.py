# Generated by Django 3.2.12 on 2022-08-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('enabled', models.BooleanField(default=True)),
                ('manual_enabled', models.BooleanField(default=True)),
                ('enabled_by_default', models.BooleanField(default=True)),
                ('management_command', models.BooleanField(default=False)),
                ('beta_command', models.BooleanField(default=False, help_text='Under development command')),
                ('custom_command', models.BooleanField(default=False, help_text='Not a default command')),
                ('private_enabled', models.BooleanField(default=True, help_text='The bot-user chat can be used')),
                ('private_only', models.BooleanField(default=False, help_text='Can be used only with bot-user chat')),
                ('pro_command', models.IntegerField(default=0, help_text='Pro level required to use the command')),
                ('permissions', models.IntegerField(default=0, help_text='Permissions required to use the command')),
                ('cost', models.IntegerField(default=0)),
                ('hourly_max_uses', models.IntegerField(default=0)),
                ('daily_max_uses', models.IntegerField(default=0)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='command.category')),
            ],
        ),
        migrations.CreateModel(
            name='CommandArg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arg', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=60)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handled_args', to='command.command')),
            ],
        ),
        migrations.CreateModel(
            name='CommandParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=60)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handled_params', to='command.command')),
            ],
        ),
        migrations.CreateModel(
            name='CommandParamDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en-US', 'English'), ('it-IT', 'Italian')], default='en-us', max_length=5)),
                ('description', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=50)),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='command_param', to='command.commandparam')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommandDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en-US', 'English'), ('it-IT', 'Italian')], default='en-us', max_length=5)),
                ('description', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='command_description', to='command.command')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommandArgDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en-US', 'English'), ('it-IT', 'Italian')], default='en-us', max_length=5)),
                ('description', models.CharField(max_length=30)),
                ('example', models.CharField(max_length=50)),
                ('arg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='command_arg', to='command.commandarg')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='commandparam',
            constraint=models.UniqueConstraint(fields=('command', 'param'), name='unique_param'),
        ),
        migrations.AddConstraint(
            model_name='commandarg',
            constraint=models.UniqueConstraint(fields=('command', 'arg'), name='unique_arg'),
        ),
    ]
