from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension


@login_required
def editar_usuario(request):
    
    user_extension_logued, _ =UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form= EditFullUser(request.POST, request.FILES)
        
        if form.is_valid():
           
            request.user.email=form.cleaned_data["email"]
            request.user.first_name=form.cleaned_data["first_name"]
            request.user.last_name=form.cleaned_data["last_name"]
            request.user.email=form.cleaned_data["email"]
            user_extension_logued.avatar=form.cleaned_data["avatar"]
            user_extension_logued.link=form.cleaned_data["link"]
            user_extension_logued.more_description=form.cleaned_data["more_description"]
            
            if form.cleaned_data["password1"] !="" and form.cleaned_data["password1"]==form.cleaned_data["password2"]:
                request.user.set_password(form.cleaned_data["password1"])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect("pymeapp")
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

@login_required
def usuario_datos(request):
    mas_datos, _ =UserExtension.objects.get_or_create(user=request.user)
    return render(request, "blog/usuario_datos.html", {"mas_datos": mas_datos})

