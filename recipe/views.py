from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Recipe
from django.db.models import Q
from django.contrib import messages
from .forms import RecipeForm
from django.forms.models import model_to_dict

# Create your views here.
@login_required(login_url="login")
def recipe_create_view(request):
    form = RecipeForm()
    if request.method == 'POST':

        form = RecipeForm(request.POST)
        if(form.is_valid()):
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            return redirect("/recipe_detail.html")

    context={
        "form":form
    }
    return render(request,"recipe/recipe_create.html",context)

@login_required(login_url="login")
def recipe_delete(request, id):

    recipe = Recipe.objects.get(pk = id)
    if recipe is not None:
        recipe.delete()
        return redirect("/recipe_detail.html")

    messages.info(request,"Recipe not found!")
    return redirect("/recipe_detail.html")

@login_required(login_url="login")
def recipe_edit(request, id):
    recipe = Recipe.objects.get(pk=id)
    if recipe is not None and request.user == recipe.author:
        form=RecipeForm(initial=model_to_dict(recipe))
    if request.method == 'POST':
        form=RecipeForm(request.POST, instance=recipe)
        if(form.is_valid()):
            form.save()
            return redirect("/recipe_view.html/"+id+"/")

    context={
        "form":form
    }
    return render(request,"recipe/recipe_edit.html",context)



@login_required(login_url="login")
def recipe_detail_view(request):

    if request.method == 'GET':
        search = request.GET.get('Search')
        name = request.GET.get('name')
        cuisine = request.GET.get('cuisine')
        ingredients = request.GET.get('ingredients')

        if name == cuisine == ingredients is None:

            if search is not None:
                lookups = Q(name__icontains=search) #| Q(__icontains=query)

                obj = Recipe.objects.filter(lookups).distinct()

            else:
                obj = Recipe.objects.all()

        else:
            lookups = Q(name__icontains=search) | Q(cuisine__icontains=search) | Q(ingredients__icontains=search)
            obj = Recipe.objects.filter(lookups).distinct()
    else:
        obj = Recipe.objects.all()

    context = {"objs": obj}

    return render(request, 'recipe/recipe_detail.html',context)


@login_required(login_url="login")
def recipe_view(request, id):
    recipe_obj = Recipe.objects.get(pk=id);
    context={
        "recipe_objs":recipe_obj
    }
    return render(request, "recipe/recipe_view.html", context)

