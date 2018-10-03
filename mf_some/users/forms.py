from django.contrib.auth import get_user_model
from improved_user.forms import AbstractUserChangeForm

User = get_user_model()


class UserUpdateForm(AbstractUserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'short_name', 'password']
