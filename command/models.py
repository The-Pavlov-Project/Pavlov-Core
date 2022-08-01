from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Command(models.Model):
    """The command descriptor"""
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    enabled = models.BooleanField(default=True)
    manual_enabled = models.BooleanField(default=True)

    enabled_by_default = models.BooleanField(default=True)
    management_command = models.BooleanField(default=False)
    beta_command = models.BooleanField(default=False, help_text='Under development command')
    custom_command = models.BooleanField(default=False, help_text='Not a default command')
    private_enabled = models.BooleanField(default=True, help_text='The bot-user chat can be used')
    private_only = models.BooleanField(default=False, help_text='Can be used only with bot-user chat')
    pro_command = models.IntegerField(default=0, help_text='Pro level required to use the command')
    permissions = models.IntegerField(default=0, help_text='Permissions required to use the command')

    cost = models.IntegerField(default=0)
    hourly_max_uses = models.IntegerField(default=0)
    daily_max_uses = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CommandArg(models.Model):
    """Arguments in the command manual"""
    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name='handled_args')
    arg = models.CharField(max_length=30)
    example = models.CharField(max_length=60)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_arg",
                fields=('command', 'arg')
            )
        ]

    def __str__(self):
        return f'{self.command}-{self.arg}'


class CommandParam(models.Model):
    """Parameters in the command manual"""
    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name='handled_params')
    param = models.CharField(max_length=30)
    example = models.CharField(max_length=60)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_param",
                fields=('command', 'param')
            )
        ]

    def __str__(self):
        return f'{self.command}-({self.param})'


class TranslationAbstract(models.Model):
    """Language handler for the command description, args and params"""
    language = models.CharField(default='en-us', choices=settings.LANGUAGES, max_length=5)
    description = models.CharField(max_length=30)
    example = models.CharField(max_length=50)

    class Meta:
        abstract = True


class CommandDescription(TranslationAbstract):
    """A single description that define the command"""
    name = models.CharField(max_length=30)
    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name='command_description')

    def __str__(self):
        return f'{self.command}-{self.language}'


class CommandArgDescription(TranslationAbstract):
    """Translated description for Param"""
    arg = models.ForeignKey(CommandArg, on_delete=models.CASCADE, related_name='command_arg')

    def __str__(self):
        return f'{self.arg}-{self.language}'


class CommandParamDescription(TranslationAbstract):
    """Translated description for Param"""
    param = models.ForeignKey(CommandParam, on_delete=models.CASCADE, related_name='command_param')

    def __str__(self):
        return f'{self.param}-{self.language}'
