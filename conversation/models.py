from django.db import models
from item.models import Item
from django.contrib.auth.models import User


class Conversation(models.Model):
    item = models.ForeignKey(
        Item, related_name="conversations", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-modified_at",)


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name="created_messages",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        sender_username = (
            self.created_by.username if self.created_by else "Deleted User"
        )
        return f"Message by {sender_username}: {self.content[:50]}..."
