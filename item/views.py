from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, ItemImage, Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from django.db.models import Q
import os
from django.contrib import messages


def search(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category_id", 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id:
        items = items.filter(category=category_id)

    return render(
        request,
        "item/search.html",
        context={
            "items": items,
            "query": query,
            "categories": categories,
            "category_id": int(category_id),
        },
    )


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


def validate_images(images):
    """Validate uploaded image files"""
    errors = []

    # Configuration
    MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    MAX_IMAGES = 10

    if len(images) > MAX_IMAGES:
        errors.append(
            f"You can upload maximum {MAX_IMAGES} images , but you upload {len(images)} images"
        )

    for image in images:
        if image.size > MAX_IMAGE_SIZE:
            errors.append(f"File '{image.name}' is too large. Maximum size is 5MB.")

        img_ext = os.path.splitext(image.name)[1].lower()
        if img_ext not in ALLOWED_EXTENSIONS:
            errors.append(
                f"File '{image.name}' has invalid format. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
            )

        # Check if file is empty
        if image.size == 0:
            errors.append(f"File '{image.name}' is empty.")

    return errors


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        images = request.FILES.getlist("images")
        image_errors = validate_images(images)

        if form.is_valid() and not image_errors:
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            for image in images:
                ItemImage.objects.create(item=item, image=image)
            messages.success(
                request, f"Item created successfully with {len(images)} images!"
            )

            return redirect("item:detail", pk=item.id)
        else:
            for error in image_errors:
                messages.error(request, error)
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
        images = request.FILES.getlist("images")
        image_errors = []
        if images:  # if user add new images
            image_errors = validate_images(images)

        if form.is_valid() and not image_errors:
            form.save()

            if images:
                for image in images:
                    ItemImage.objects.create(item=item, image=image)
                messages.success(
                    request,
                    f"Item updated successfully! Added {len(images)} new images.",
                )
            else:
                messages.success(request, "Item updated successfully!")

            return redirect("item:detail", pk=item.id)
        else:
            for error in image_errors:
                messages.error(request, error)

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
