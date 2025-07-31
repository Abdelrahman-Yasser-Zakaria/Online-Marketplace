from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, ItemImage
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm


def search(request):
    query = request.GET.get("query", "")
    items = Item.objects.filter(is_sold=False)

    if query:
        items=items.filter(name__icontains=query)

    return render(request, "item/search.html", context={"items": items, "query": query})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )[:4]
    return render(
        request,
        "item/detail.html",
        context={"item": item, "related_items": related_items},
    )


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            images = request.FILES.getlist("images")

            for image in images:
                ItemImage.objects.create(item=item, image=image)

            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()

    return render(
        request,
        "item/form.html",
        context={
            "form": form,
            "titel": "New item",
        },
    )


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            images = request.FILES.getlist("images")

            for image in images:
                ItemImage.objects.create(item=item, image=image)

            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(
        request,
        "item/form.html",
        context={
            "form": form,
            "titel": "Edit item",
        },
    )


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")
