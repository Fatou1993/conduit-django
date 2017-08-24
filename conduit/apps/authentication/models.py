import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from conduit.apps.core.models import TimestampedModel

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.

    """
    def create_user(self, email, username, first_name, last_name, phone_number, image, gender, target, city, birthday, is_adult, accept_data_treatment, password=None):

        if username is None :
            raise TypeError('Users must have a username.')
        if first_name is None :
            raise TypeError('Users must have a first_name.')
        if last_name is None :
            raise TypeError('Users must have a last_name.')
        if phone_number is None :
            raise TypeError('Users must have a phone_number.')
        if image is None :
            raise TypeError('Users must have an image.')
        if gender is None :
            raise TypeError('Users must have a gender.')
        if target is None :
            raise TypeError('Users must have a target.')
        if city is None :
            raise TypeError('Users must have a city.')
        if birthday is None :
            raise TypeError('Users must have a birthday.')

        if is_adult is None :
            raise TypeError('Users must agree to be adult.')
        elif not is_adult:
            raise ValueError('Users must be adult.')

        if accept_data_treatment is None or not accept_data_treatment:
            raise TypeError('Users must agree the data treatment.')

        if email is None :
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), username=username, first_name=first_name, last_name=last_name, phone_number=phone_number, image=image, gender=gender, target=target, city=city, birthday=birthday, is_adult=is_adult, accept_data_treatment=accept_data_treatment)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, first_name, last_name, phone_number, image, gender, target, city, birthday, is_adult, accept_data_treatment, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None :
            return TypeError('Super users must have a password.')
        user = self.create_user(email, username, first_name, last_name, phone_number, image, gender, target, city, birthday, is_adult, accept_data_treatment, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    """
    Each `User` needs a human-readable unique identifier that we can use to
    represent the `User` in the UI. We want to index this column in the
    database to improve lookup performance.
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    image = models.URLField()

    MAN, WOMAN = 'Homme', 'Femme'
    SEXES = (
        (MAN, 'Homme'),
        (WOMAN, 'Femme')
    )
    gender = models.CharField(
        max_length=5,
        choices=SEXES
    )
    target = models.CharField(
        max_length=5,
        choices=SEXES
    )
    city = models.CharField(max_length=100, default="Dakar, Senegal")
    birthday = models.DateField()
    is_adult = models.BooleanField(default=True)
    accept_data_treatment = models.BooleanField(default=True)

    # We also need a way to contact the user and a way for the user to identify
    # themselves when logging in. Since we need an email address for contacting
    # the user anyways, we will also use the email for logging in because it is
    # the most common form of login credential at the time of writing.
    email = models.EmailField(db_index=True, unique=True)
    # When a user no longer wishes to use our platform, they may try to delete
    # their account. That's a problem for us because the data we collect is
    # valuable to us and we don't want to delete it. We
    # will simply offer users a way to deactivate their account instead of
    # letting them delete it. That way they won't show up on the site anymore,
    # but we can still analyze the data.
    is_active = models.BooleanField(default=True)
    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users this flag will always be
    # false.
    is_staff = models.BooleanField(default=False)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'image', 'gender', 'target', 'city', 'birthday', 'is_adult', 'accept_data_treatment']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.first_name + ' '+ self.last_name

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now()+timedelta(days=60)
        token = jwt.encode({
            'id':self.pk,
            'exp':int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')



