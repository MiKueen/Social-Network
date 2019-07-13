from django.core.exceptions import ValidationError


def validate_content(value):
    content = value
    if content == 'Male' or content == 'Female' or content == 'Others':

        return value
    raise ValidationError('Please Enter values among these only Male/Female/Others')
