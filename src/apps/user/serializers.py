from djoser.serializers import UserCreateSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'password', 'first_name', 'last_name', 'username')