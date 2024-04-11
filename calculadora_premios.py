def generar_estructura(names,goals,goals_avoided,assists):
    player_stats= []
    for name,goal,goal_avoided,assist in zip(names,goals,goals_avoided,assists):
        player_stats.append({
            "Nombre": name,
            "Goles":goal,
            "Goles evitados": goal_avoided,
            "Asistencias":assist
        })
    return player_stats

def nombre_goles_goleador(player_stats):
    max=0
    max_goal_name=""
    for player in player_stats:
        if player["Goles"] > max:
            max= player["Goles"]
            max_goal_name= player["Nombre"]
    
    return max_goal_name,max

def mas_influyente(player_stats):
    max_list=[]
    for player in player_stats:
        max_list.append((player["Nombre"],(sum([player["Goles"]*1.5,player["Goles evitados"]*1.25,player["Asistencias"]]))/3))
    return max_list    
        
def promedio_goles_equipo(goals):
    return (sum(goals)/25)

def promedio_goles_goleador(goals_converted):
    return goals_converted/25
