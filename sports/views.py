from django.shortcuts import render

# Create your views here.

import requests

def sport_list(request):
    return render(request,'sports/sport_list.html')


def sport_cricket(request):
    url = 'http://api.sportradar.us/cricket-t2/en/schedules/2018-11-01/schedule.json?api_key=grbd3ehrnc4e2d5xkauxpds3'
    json_data = requests.get(url).json()
    name = json_data['sport_events'][0]['tournament']['name']
    venue = json_data['sport_events'][0]['venue']['name']
    city = json_data['sport_events'][0]['venue']['city_name']
    capacity = json_data['sport_events'][0]['venue']['capacity']
    return render(request,'sports/stats_cricket.html',{'name': name,'venue':venue,'city': city, 'capacity':capacity})


def sport_nba(request):
    url = 'http://api.sportradar.us/nba/trial/v5/en/games/2018/11/01/schedule.json?api_key=4s85khb3qpwyd2rjjkg4cazq'
    json_data = requests.get(url).json()
    name = json_data['league']['name']
    venue_zone_name = json_data['games'][0]['time_zones']['venue']
    venue_name = json_data['games'][0]['venue']['name']
    capacity = json_data['games'][0]['venue']['capacity']
    name1 = json_data['league']['name']
    venue_zone_name1 = json_data['games'][1]['time_zones']['venue']
    venue_name1 = json_data['games'][1]['venue']['name']
    capacity1 = json_data['games'][1]['venue']['capacity']
    name2 = json_data['league']['name']
    venue_zone_name2 = json_data['games'][2]['time_zones']['venue']
    venue_name2 = json_data['games'][2]['venue']['name']
    capacity2 = json_data['games'][2]['venue']['capacity']
    return render(request,'sports/stats_nba.html',{'name':name, 'venue_zone_name': venue_zone_name,'venue_name': venue_name,
                                                   'capacity': capacity,'name1':name1,'venue_zone_name1':venue_zone_name1,
                                                   'venue_name1':venue_name1,'capacity1':capacity1,'name2':name2,'venue_zone_name2':venue_zone_name2,
                                                   'venue_name2':venue_name2,'capacity2':capacity2})
