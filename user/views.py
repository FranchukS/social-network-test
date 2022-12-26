from django.contrib.auth import get_user_model
from rest_framework import generics

from user.serializers import UserSerializer, UserActivitySerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ListUserView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserActivitySerializer

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Retrieve the user with filter"""
        user_ids = self.request.query_params.get("user_id")
        username = self.request.query_params.get("username")

        queryset = get_user_model().objects.all()
        print(queryset)
        if user_ids:
            user_ids = self._params_to_ints(user_ids)
            queryset = queryset.filter(id__in=user_ids)

        if username:
            queryset = queryset.filter(username__icontains=username)

        return queryset
