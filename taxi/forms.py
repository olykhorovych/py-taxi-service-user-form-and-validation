from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from taxi.models import Car, Driver


class DriverCreatForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number", )


class DriverUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Driver
        fields = ("username", "first_name", "last_name", "email")
        exclude = ("password", )


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Driver
        fields = ("license_number", )
