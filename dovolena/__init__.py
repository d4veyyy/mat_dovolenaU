from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_rating(value):
    if value < 1 or value > 5:
        raise ValidationError(
            _('Hodnocení musí být mezi 1 a 5.'),
            params={'value': value},
        )
