from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("bio",)

class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields