from django import forms

from .models import Profile, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'profile_picture']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class ProfileCreateForm(ProfileBaseForm):
    pass

class ProfileDetailsForm(ProfileBaseForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.save()
    #     return object





class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
        }


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
