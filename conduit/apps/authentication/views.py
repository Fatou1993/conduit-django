from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    RegistrationSerializer, LoginSerializer, UserSerializer
)
from .renderers import UserJSONRenderer

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):

        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user_data = request.data.get('user', {})
        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'first_name': user_data.get('first_name', request.user.first_name),
            'last_name': user_data.get('last_name', request.user.last_name),
            'phone_number': user_data.get('phone_number', request.user.phone_number),
            'image': user_data.get('image', request.user.image),
            'gender': user_data.get('gender', request.user.gender),
            'target': user_data.get('target', request.user.target),
            'city': user_data.get('city', request.user.city),
            'birthday': user_data.get('birthday', request.user.birthday),
            'email': user_data.get('email', request.user.email),
            'profile': {
                'bio': user_data.get('bio', request.user.profile.bio),
                'want_to_marry_within_how_many_years': user_data.get('want_to_marry_within_how_many_years', request.user.profile.want_to_marry_within_how_many_years),
                'marital_status': user_data.get('marital_status', request.user.profile.marital_status),
                'number_of_children': user_data.get('number_of_children', request.user.profile.number_of_children),
                'want_children': user_data.get('want_children', request.user.profile.want_children),
                'studies_level': user_data.get('studies_level', request.user.profile.studies_level),
                'height': user_data.get('height', request.user.profile.height),
                'silhouette': user_data.get('silhouette', request.user.profile.silhouette),
                'origin': user_data.get('origin', request.user.profile.origin),
                'religion': user_data.get('religion', request.user.profile.religion),
                'ethny': user_data.get('ethny', request.user.profile.ethny),
                'smoking': user_data.get('smoking', request.user.profile.smoking),
                'confrery': user_data.get('confrery', request.user.profile.confrery),
                'min_age': user_data.get('min_age', request.user.profile.min_age),
                'max_age': user_data.get('max_age', request.user.profile.max_age),
                'ideal_marital_status': user_data.get('ideal_marital_status', request.user.profile.ideal_marital_status),
                'ideal_want_children': user_data.get('ideal_want_children',
                                                      request.user.profile.ideal_want_children),
                'ideal_height': user_data.get('ideal_height', request.user.profile.ideal_height),
                'ideal_silhouette': user_data.get('ideal_silhouette', request.user.profile.ideal_silhouette),
                'ideal_smoking': user_data.get('ideal_smoking', request.user.profile.ideal_smoking),
                'ideal_confrery': user_data.get('ideal_confrery', request.user.profile.ideal_confrery),
                'ideal_religion': user_data.get('ideal_religion', request.user.profile.ideal_religion),
                'ideal_ethny': user_data.get('ideal_ethny', request.user.profile.ideal_ethny)
            }
        }
        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationAPIView(APIView):

    #Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
