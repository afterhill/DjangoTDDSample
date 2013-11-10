from django import forms
from lists.models import Item

EMPTY_LIST_ERROR = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.models.ModelForm, self).__init__(*args, **kwargs)
        empty_error = "You can't have an empty list item"
        self.fields['text'].error_messages['required'] = EMPTY_LIST_ERROR

    def save(self, for_list):
        self.instance.list = for_list
        return super(forms.models.ModelForm, self).save()

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                                           'placeholder': 'Enter a to-do item',
                                           'class': 'form-control input-lg',
                                           })
        }
