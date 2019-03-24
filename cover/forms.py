from urllib.parse import urlencode
from django import forms
from .utils import COLOR_CODES


class CoverForm(forms.Form):
    COLOR_CHOICES = [(i, str(COLOR_CODES[i])) for i in range(len(COLOR_CODES))]

    title = forms.CharField()
    top_text = forms.CharField()
    author = forms.CharField()
    animal_code = forms.ChoiceField(choices=[(i, i) for i in range(1, 41)])
    color_code = forms.ChoiceField(choices=COLOR_CHOICES)
    guide_text = forms.CharField()
    guide_text_placement = forms.ChoiceField(
        choices=[
            ('bottom_right', 'Bottom Right'),
            ('bottom_left', 'Bottom Left'),
            ('top_right', 'Top Right'),
            ('top_left', 'Top Left'),
        ]
    )

    @property
    def get_params(self):
        if hasattr(self, 'cleaned_data'):
            return urlencode(self.cleaned_data)
        return None
