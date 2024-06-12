from django.db import models
from django.core.exceptions import ValidationError


class Ucastnik(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno účastníka', help_text='Zadejte jméno účastníka',
                             error_messages={'blank': 'Jméno účastníka musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení účastníka',
                                help_text='Zadejte příjmení účastníka',
                                error_messages={'blank': 'Příjmení účastníka musí být vyplněno'})
    email = models.CharField(max_length=50, verbose_name='E-mail účastníka', help_text='Zadejte E-mail účastníka',
                             error_messages={'blank': 'E-mail účastníka musí být vyplněný'})
    telefon = models.IntegerField(max_length=9, verbose_name='Telefon účastníka', help_text='Zadejte telefonní číslo',
                                  error_messages={'blank': 'Telefon účastníka musí být vyplněný'})
    datum_narozeni = models.DateField(verbose_name='Datum narození účastníka', help_text='Zadejte datum narození',
                                      error_messages={'blank': 'Datum narození musí být vyplněný'})

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Účastník'
        verbose_name_plural = 'Účastníci'

    def __str__(self):
        return f'{self.prijmeni} {self.jmeno} {self.email} {self.telefon} {self.datum_narozeni}'


class Dovolena(models.Model):
    destinace = models.CharField(max_length=20, blank=True, null=True, verbose_name='Destinace',
                                 help_text='Zadejte destinace')
    zacatek_terminu = models.DateField(verbose_name='Začátek dovolené', help_text='Zadejte záčátek vaší dovolené',
                                       error_messages={'blank': 'Začátek termínu musí být vyplněný'})
    konec_terminu = models.DateField(verbose_name='Konec dovolené', help_text='Zadejte konec vaší dovolené',
                                     error_messages={'blank': 'Konec termínu musí být vypněný'})

    class Flight(models.Model):
        AIRPORT_CHOICES = (
            ('BRNO', 'Brno'),
            ('PRAHA', 'Praha'),
            ('OSTRAVA', 'Ostrava'),
        )

        misto_odletu = models.CharField(max_length=7, choices=AIRPORT_CHOICES, verbose_name='Místo odletu',
                                        help_text='Zadej místo odletu', error_messages={'blank': 'Místo odletu musí být'
                                                                                                 'zadáno'})

        def __str__(self):
            return f"{self.misto_odletu}"

    class Meta:
        verbose_name = "Dovolená"
        verbose_name_plural = "Dovolené"
        ordering = ['destinace', 'zacatek_terminu', 'konec_terminu']

    def __str__(self):
        return f"{self.destinace} {self.zacatek_terminu} {self.konec_terminu} "


class Rezervace(models.Model):
    pocet_ucastniku = models.IntegerField(
        verbose_name='Počet účastníků',
        help_text='Zadejte počet účastníků',
        error_messages={'blank': 'Počet účastníků musí být vyplněný'}
    )
    celkem_cena = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Celková cena',
        help_text='Zadejte celkovou cenu',
        error_messages={'blank': 'Celková cena musí být vyplněná'}
    )

    class Meta:
        verbose_name = "Rezervace"
        verbose_name_plural = "Rezervace"
        ordering = ['Rezervace']

    def __str__(self):
        return f"Rezervace {self.id} - Počet účastníků: {self.pocet_ucastniku}, Cena: {self.celkem_cena}"


def validate_rating(value):
    if value < 1 or value > 5:
        raise ValidationError(
            'Hodnocení musí být mezi 1 a 5.',
            params={'value': value},
        )


class Recenze(models.Model):
    recenze_id = models.AutoField(primary_key=True)
    rating = models.IntegerField(
        verbose_name="Rating",
        help_text="Hodnocení musí být mezi 1 a 5",
        validators=[validate_rating]
    )
    review = models.TextField(
        verbose_name="Recenze",
        blank=True,
        null=True,
        help_text="Přidejte recenzi"
    )

    class Meta:
        verbose_name = "Recenze"
        verbose_name_plural = "Recenze"
        ordering = ['recenze_id']

    def __str__(self):
        return f"Recenze {self.recenze_id}"
