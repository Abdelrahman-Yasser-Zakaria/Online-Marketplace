from django import forms
from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border border-gray-300 focus:border-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-300 transition-colors duration-200"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "condition",
            "category",
            "name",
            "description",
            "price",
            "location",
        )

        widgets = {
            "condition": forms.Select(attrs={"class": INPUT_CLASSES}),
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "location": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Enter city, country (e.g., Cairo, Egypt)",
                }
            ),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "condition",
            "category",
            "name",
            "description",
            "price",
            "location",
            "is_sold",
        )

        widgets = {
            "condition": forms.Select(attrs={"class": INPUT_CLASSES}),
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "location": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Enter city, country (e.g., Cairo, Egypt)",
                }
            ),
        }
