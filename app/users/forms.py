from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username_field = settings.ACCOUNT_USER_MODEL_USERNAME_FIELD

        username = self.cleaned_data.get(username_field, self.cleaned_data.get('username', None))

        kwargs = {username_field: username}

        try:
            User.objects.get(**kwargs)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])
