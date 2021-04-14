from django.core.validators import URLValidator


def validate_url(url):
    """Validate url link provided by user
    In case of error function will throw ValidationError"""
    URLValidator(url)
