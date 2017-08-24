from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    phone_number = serializers.CharField(source='user.phone_number')
    image = serializers.CharField(source='user.image')
    gender = serializers.CharField(source='user.gender')
    target = serializers.CharField(source='user.target')
    city = serializers.CharField(source='user.city')
    birthday = serializers.CharField(source='user.birthday')

    marital_status = serializers.ChoiceField(
        choices=["Celibataire", 'Marrie(e)', "Jamais Marrie(e)", "Divorce(e)", "Veuf(ve)"],
        source='profile.marital_status', read_only=True)

    studies_level = serializers.ChoiceField(
        choices=['AVANT BFEM', 'BFEM', 'BAC', 'BAC+2', 'BAC+3', 'BAC+4', 'BAC+5 et plus'],
        source='profile.studies_level', read_only=True)
    silhouette = serializers.ChoiceField(choices=['Normale', 'Sportif/ve', 'En surpoids'], source='profile.silhouette',
                                         read_only=True)
    origin = serializers.ChoiceField(choices=['Africaine', 'Europeene', 'Asiatique', 'Arabe'], source='profile.origin',
                                     read_only=True)
    religion = serializers.ChoiceField(choices=['Musulman', 'Chretien', 'Autre'], source='profile.religion',
                                       read_only=True)
    ethny = serializers.ChoiceField(choices=['Wolof', 'Peul', 'Toucouleur', 'Serere', 'Diola', 'Autre'],
                                    source='profile.ethny', read_only=True)
    confrery = serializers.ChoiceField(choices=['Mouride', 'Tidjane', 'Layene', 'Autre'], source='profile.confrery',
                                       read_only=True)
    ideal_marital_status = serializers.ChoiceField(
        choices=["Celibataire", 'Marrie(e)', "Jamais Marrie(e)", "Divorce(e)", "Veuf(ve)"],
        source='profile.ideal_marital_status', read_only=True)
    ideal_silhouette = serializers.ChoiceField(choices=['Normale', 'Sportif/ve', 'En surpoids'],
                                               source='profile.ideal_silhouette',
                                               read_only=True)
    ideal_religion = serializers.ChoiceField(choices=['Musulman', 'Chretien', 'Autre'], source='profile.ideal_religion',
                                             read_only=True)
    ideal_ethny = serializers.ChoiceField(choices=['Wolof', 'Peul', 'Toucouleur', 'Serere', 'Diola', 'Autre'],
                                          source='profile.ideal_ethny', read_only=True)
    ideal_confrery = serializers.ChoiceField(choices=['Mouride', 'Tidjane', 'Layene', 'Autre'],
                                             source='profile.ideal_confrery',
                                             read_only=True)
    class Meta :
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'image', 'gender', 'target', 'city', 'birthday',
                  'want_to_marry_within_how_many_years', 'marital_status', 'number_of_children', 'want_children', 'studies_level', 'height', 'silhouette', 'origin',
                  'religion', 'ethny', 'smoking', 'confrery', 'bio', 'min_age', 'max_age', 'ideal_marital_status', 'ideal_want_children', 'ideal_height', 'ideal_silhouette', 'ideal_smoking',
                  'ideal_confrery', 'ideal_religion', 'ideal_ethny')
        read_only_fields = ('username', 'first_name', 'last_name', )