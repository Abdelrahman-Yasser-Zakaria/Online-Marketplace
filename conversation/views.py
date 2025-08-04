from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ConversationMessageForm
from .models import Conversation
from item.models import Item


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    conversations = Conversation.objects.filter(item=item).filter(
        members__in=[request.user]
    )

    if conversations:# redirect the user to this conversation
        return redirect("conversation:detail",pk=conversations.first().id)  

    if request.method == "POST":
        form = ConversationMessageForm(
            request.POST
        )  # to get the content of the message

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("conversation:detail", pk=conversation.id)

    else:
        form = ConversationMessageForm()

    return render(request, "conversation/new.html", context={"form": form})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user])

    return render(
        request, "conversation/inbox.html", context={"conversations": conversations}
    )

@login_required
def detail(request,pk):
    conversation = Conversation.objects.filter(members__in=[request.user]).get(pk=pk)

    if request.method == "POST":
        form = ConversationMessageForm(
            request.POST
        )  # to get the content of the message

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect("conversation:detail", pk=pk)

    else:
        form = ConversationMessageForm()

    return render(
        request, "conversation/detail.html", context={"conversation": conversation,"form":form}
    )
