from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border border-gray-300 focus:border-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-300 transition-colors duration-200"}
            )
        }
