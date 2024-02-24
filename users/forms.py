from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    """ This is a Create form for user object used in django admin panel """
    class Meta:
        model = User
        fields = ("email", "full_name")


class CustomUserChangeForm(UserChangeForm):
    """ This is a edit form for user object used in django admin panel """
    class Meta:
        model = User
        fields = ("email", "full_name")