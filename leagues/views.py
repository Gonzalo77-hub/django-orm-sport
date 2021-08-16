from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Avg, Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"leagues_mujeres": League.objects.filter(name__icontains='Womens'),
		"leagues_hockey": League.objects.filter(name__icontains='Hockey'),
		"leagues_no_football": League.objects.exclude(sport__icontains='football'),
		"leagues_no_name_conference": League.objects.filter(name__icontains='Conference'),
		"leagues_region_atlantida":League.objects.filter(name__icontains='atlantic'),
		"teams_dallas": Team.objects.filter(location__icontains='Dallas'),
		"teams_raptors": Team.objects.filter(team_name__icontains='raptors'),
		"teams_city": Team.objects.filter(location__icontains='city'),
		"teams_start": Team.objects.filter(team_name__startswith='T'),
		"teams_alfa": Team.objects.order_by("location"),
		"teams_inv": Team.objects.order_by('-team_name'),
		"players_cooper": Player.objects.filter(last_name__contains='Cooper'),
		"players_joshua": Player.objects.filter(first_name__contains='Joshua'),
		"players_cooper_ex": Player.objects.filter(last_name__contains='Cooper').exclude(first_name__contains="Joshua"),
		"players_alex_wyatt": Player.objects.filter(first_name__contains='Alexander') | Player.objects.filter(first_name__contains='Wyatt'),

		"teams_atlantic_soccer":Team.objects.filter(league__name__contains='Atlantic Soccer Conference'),
		"player_penguins":Player.objects.filter(curr_team__team_name__contains='Penguins'),
		"player_international":Player.objects.filter(curr_team__league__name__contains='International Collegiate Baseball Conference'),
		"player_american":Player.objects.filter(curr_team__league__name__contains='American Conference of Amateur Football') & Player.objects.filter(last_name__contains='Lopez'),
		"player_futbol":Player.objects.filter(curr_team__league__sport__contains='football'),
		"teams_sophia":Team.objects.filter(curr_players__first_name__contains='Sophia'),
		"league_sophia":League.objects.filter(teams__curr_players__first_name__contains='Sophia'),
		"player_Flores":Player.objects.filter(last_name__contains='flores') & Player.objects.exclude(curr_team__team_name='Roughriders'),
		"teams_evans":Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		"players_maniota":Player.objects.filter(all_teams__team_name__icontains="Tiger", all_teams__location="Manitoba"),
		"players_vikings":Player.objects.filter(all_teams__team_name__icontains="Vikings", all_teams__location="Wichita").exclude(curr_team__team_name='Vikings', all_teams__location='Wichita'),
		"team_jacob":Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name='Colts', location='Oregon'),
		"players_joshua":Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players" ),
		"teams_12": Team.objects.annotate( c= Count("all_players")).filter(c__gt=11),
		"All_players": Player.objects.annotate( b= Count("all_teams")).order_by("-b"),



	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("/")