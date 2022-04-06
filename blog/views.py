from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension


@login_required
def editar_usuario(request):
    
    user_extension_logued, _ =UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form= EditFullUser(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            #return render(request, "blog/index.html", {"msj": f"Se crea correctamente al usuario {username}"})
            return redirect("login")
        else:
            return render(request, "blog/editar_usuario.html", {"form": form, "msj": "El formulario no es valido"})
    
    
    form = EditFullUser(
        initial={
        "email": request.user.email,
        "password1": "",
        "password2": "",
        "first_name":request.user.first_name,
        "last_name": request.user.last_name,
        "avatar": user_extension_logued.avatar,
        "link": user_extension_logued.link,
        "more_description": user_extension_logued.more_description
        })
    return render(request, "blog/editar_usuario.html", {"form": form})

