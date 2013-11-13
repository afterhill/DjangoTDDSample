from django import forms
from lists.models import Item
from django.core.exceptions import ValidationError

EMPTY_LIST_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


class ItemForm(forms.models.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['text'].error_messages['required'] = EMPTY_LIST_ERROR

    def save(self):
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


class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super(ExistingListItemForm, self).__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError:
            self._update_errors({'text': [DUPLICATE_ITEM_ERROR]})
