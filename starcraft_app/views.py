from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player


def index(request):
    return render(request, "player_list/home.html")

def p_list_view(request):
    player_list = Player.objects.order_by('ingame_name')
    context = {
        "player_list": player_list
    }
    print(player_list)
    return render(request, "player_list/player_view.html", context=context)
   
def add_player(request):
    if request.method == "POST":
        new_player = Player(fname=request.POST["fname"],
                            lname=request.POST["lname"],
                            ingame_name=request.POST["ingame_name"],
                            country=request.POST["country"],
                            team=request.POST["team"],
                            race=request.POST["race"])
        new_player.save()
        return redirect("p_list")
    return render(request, "player_list/add_player.html")

def p_edit(request, id):
    player = Player.objects.get(id=id)
    if request.method == "POST":
        for key, value in request.POST.items():
            if(value and key != "csrfmiddlewaretoken"):
                setattr(player, key, value)
        player.save()
        return redirect("p_list")
    context = {
        "p": player
    }
    player.save()
    return render(request, "player_list/player_edit.html", context=context)

def p_delete(request, id):
    player_delete = Player.objects.get(id=id)
    player_delete.delete()
    return redirect("p_list")

def confirm_delete(request, id):
    context = {
        "id": id
    }
    return render(request, "player_list/confirm_delete.html", context=context)

def t_list_view(request):
    all_players = Player.objects.all()
    team_list = {}
    for p in all_players:
        if p.team in team_list.keys():
            team_list[p.team].append(p)
        else:
            team_list.update({p.team:[p]})
    print(team_list)

    context = {
        "team_list" : team_list
    }

    return render(request, "player_list/team_view.html", context=context)   
