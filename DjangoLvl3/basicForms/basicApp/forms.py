from django import forms
from django.core import validators

# SAMPLE FUNCTION FOR CUSTOM-MADE FORM VALIDATION; Note that this
# runs even when not directly called, just when the below FormName class is called.

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with Z!")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match")

    # Original manually coded bot validation
    # def clean_botCatcher(self):
    #     botCatcher = self.cleaned_data['botCatcher']
    #     if len(botCatcher) > 0:
    #         raise forms.ValidationError("Gotcha bot!!!")
    #     return botCatcher
