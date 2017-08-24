from django.db import models
from django.core.validators import MinValueValidator
from conduit.apps.core.models import TimestampedModel

class Profile(TimestampedModel):

    # There is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    ##Personal Info Not Required
    want_to_marry_within_how_many_years = models.PositiveIntegerField(blank=True, default=0)
    SINGLE, MARRIED, NEVER_BEEN_MARRIED, DIVORCED, WIDOW = 'Celibataire', 'Marrie(e)', "Jamais Marrie(e)", "Divorce(e)", "Veuf(ve)"
    MARITAL_STATUS_CHOICES = (
        (SINGLE, "Celibataire"),
        (MARRIED, "Marrie(e)"),
        (NEVER_BEEN_MARRIED, "Jamais Marrie(e)"),
        (DIVORCED, "Divorce(e)"),
        (WIDOW, "Veuf(ve)")
    )
    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES,
        blank=True
    )
    number_of_children = models.PositiveIntegerField(blank=True, default=0)
    want_children = models.BooleanField(default=True)

    BEFORE_BFEM, BFEM, BAC, BAC_PLUS_TWO, BAC_PLUS_THREE, BAC_PLUS_FOUR, BAC_PLUS_FIVE_AND_PLUS = 'AVANT BFEM', 'BFEM', 'BAC', 'BAC+2', 'BAC+3', 'BAC+4', 'BAC+5 et plus'
    STUDIES_LEVEL_CHOICE = (
        (BEFORE_BFEM, "AVANT BFEM"),
        (BFEM, 'BFEM'),
        (BAC, 'BAC'),
        (BAC_PLUS_TWO, 'BAC+2'),
        (BAC_PLUS_THREE, 'BAC+3'),
        (BAC_PLUS_FOUR, 'BAC+4'),
        (BAC_PLUS_FIVE_AND_PLUS, 'BAC+5 et plus')

    )
    studies_level = models.CharField(
        max_length=30,
        choices=STUDIES_LEVEL_CHOICE,
        blank=True
    )

    height = models.PositiveIntegerField(null=True)

    SLIM, NORMAL, ATHLETIC, OVERWEIGHT = 'Mince', 'Normale', 'Sportif/ve', 'En surpoids'
    SILHOUETTE_CHOICE = (
        (SLIM, 'Mince'),
        (NORMAL, 'Normale'),
        (ATHLETIC, 'Sportif/ve'),
        (OVERWEIGHT, 'En surpoids')

    )
    silhouette = models.CharField(
        max_length=30,
        choices=SILHOUETTE_CHOICE,
        blank=True
    )

    AFRICAN, EUROPEAN, ASIATIQUE, ARABIC = 'Africaine', 'Europeene', 'Asiatique', 'Arabe'
    ORIGIN_CHOICES = (
        (AFRICAN, 'Africaine'),
        (EUROPEAN, 'Europeene'),
        (ASIATIQUE, 'Asiatique'),
        (ARABIC, 'Arabe')
    )
    origin = models.CharField(
        max_length=30,
        choices=ORIGIN_CHOICES,
        blank=True
    )
    #add_column:users,:nationality,:string

    MUSLIM, CHRISTIAN, OTHER = 'Musulman', 'Chretien', 'Autre'
    RELIGION_CHOICES = (
        (MUSLIM, 'Musulman'),
        (CHRISTIAN, 'Chretien'),
        (OTHER, 'Autre')
    )
    religion = models.CharField(
        max_length=30,
        choices=RELIGION_CHOICES,
        blank=True
    )

    WOLOF, PEUL, TOUCOULEUR, SERERE, DIOLA, OTHER = 'Wolof', 'Peul', 'Toucouleur', 'Serere', 'Diola', 'Autre'
    ETHNY_CHOICES = (
        (WOLOF, 'Wolof'),
        (PEUL, 'Peul'),
        (TOUCOULEUR, 'Toucouleur'),
        (SERERE, 'Serere'),
        (DIOLA, 'Diola'),
        (OTHER, 'Autre')
    )
    ethny = models.CharField(
        max_length=30,
        choices=ETHNY_CHOICES,
        blank=True
    )

    smoking = models.BooleanField(default=False)

    MOURIDE, TIDJANE, LAYENE, OTHER = 'Mouride', 'Tidjane', 'Layene', 'Autre'
    CONFRERY_CHOICES = (
        (MOURIDE, 'Mouride'),
        (TIDJANE, 'Tidjane'),
        (LAYENE, 'Layene'),
        (OTHER, 'Autre')
    )
    confrery = models.CharField(
        max_length=30,
        choices=CONFRERY_CHOICES,
        blank=True
    )

    bio = models.TextField(blank=True)

    # Looking in the partner
    min_age = models.PositiveIntegerField(validators=[MinValueValidator(18)], null=True)
    max_age = models.PositiveIntegerField(null=True)
    ideal_marital_status = models.CharField(
        choices=MARITAL_STATUS_CHOICES,
        max_length=20,
        blank=True
    )
    ideal_want_children = models.BooleanField(default=True)
    ideal_height = models.PositiveIntegerField(null=True)
    ideal_silhouette = models.CharField(
        max_length=30,
        choices=SILHOUETTE_CHOICE,
        blank=True
    )
    ideal_smoking = models.BooleanField(default=False)
    ideal_confrery = models.CharField(
        max_length=30,
        choices=CONFRERY_CHOICES,
        blank=True
    )
    ideal_religion = models.CharField(
        max_length=30,
        choices=RELIGION_CHOICES,
        blank=True
    )
    ideal_ethny = models.CharField(
        max_length=30,
        choices=ETHNY_CHOICES,
        blank=True
    )

    def __str__(self):
        return self.user.username


