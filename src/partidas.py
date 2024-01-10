from collections import namedtuple, defaultdict
import csv
from datetime import datetime, date, time

Partida = namedtuple("Partida", "pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2,\
 movimiento_final, combo_finish, ganador")

def booleano(cadena:str)->bool:
    if cadena.strip() == "1":
        res = True
    elif cadena.strip() == "0":
        res = False
    return res

def parser(cadena:str)->list[str]:
    cadena = cadena.replace('[', '')
    cadena = cadena.replace(']', '')
    return [i.strip() for i in cadena.split(',')]

def lee_partidas(fichero:str)->list[Partida]:
    res = []
    with open (fichero, 'rt', encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ',')
        next (lector)
        for pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2,\
                movimiento_final, combo_finish, ganador in lector:
            puntuacion = int(puntuacion)
            tiempo = float(tiempo)
            fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
            golpes_pj1 = parser(golpes_pj1)
            golpes_pj2 = parser(golpes_pj2)
            combo_finish = booleano(combo_finish)
            res.append(Partida(pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2,\
                movimiento_final, combo_finish, ganador))
    return res

def victoria_mas_rapida(partidas:list[Partida])->tuple[str, str, float]:
    res = [(i.pj1, i.pj2, i.tiempo) for i in partidas]
    return sorted(res, key = lambda x:x[2])[0]

def top_ratio_media_personajes(partidas:list[Partida], n:int)->list[str]:
    aux = defaultdict(list)
    aux2 = defaultdict(float)
    lista = []
    res = []
    for i in partidas:
        if i.pj1 == i.ganador:
            aux[i.pj1].append(i.puntuacion / i.tiempo)
        elif i.pj2 == i.ganador:
            aux[i.pj2].append(i.puntuacion / i.tiempo)
    for c,v in aux.items():
        aux2[c] = sum(v) / len(v)
    lista = sorted(aux2.items(), key = lambda x:x[1])
    for i in lista:
        res.append(i[0])
    return res[:n]

def enemigos_mas_debiles(partidas:list[Partida], personaje:str)->tuple[list[str], float]:
    aux = defaultdict(list)
    res = list()
    aux2 = defaultdict(int)
    for i in partidas:
        if i.ganador == personaje:
            aux[(i.pj1, i.pj2)].append(i.ganador)
    for c,v in aux.items():
        aux2[c] = len(v)
    for c,v in aux2.items():
        if c[0] != personaje and v == max(aux2.items(), key = lambda x:x[1])[1]:
            res.append(c[0])
        elif c[1] != personaje and v == max(aux2.items(), key = lambda x:x[1])[1]:
            res.append(c[1])
    return (res, max(aux2.items(), key = lambda x:x[1])[1])

def movimientos_comunes(partidas:list[Partida], personaje1:str, personaje2:str)->list[str]:
    res = []
    for i in partidas:
        if (i.pj1 == personaje1 and i.pj2 == personaje2) or (i.pj2 == personaje1 and i.pj1 == personaje2):
            golpes1 = {j for j in i.golpes_pj1}
            golpes2 = {j for j in i.golpes_pj2}
    for elem1, elem2 in zip(golpes1, golpes2):
        if elem1 in golpes2:
            res.append(elem1)
    return res

def cambiar_fecha(n:int)->str:
    if n == 1:
        res = "lunes"
    elif n == 2:
        res = "martes"
    elif n == 3:
        res = "miercoles"
    elif n == 4:
        res = "jueves"
    elif n == 5:
        res = "viernes"
    elif n == 6:
        res = "sabado"
    elif n == 7:
        res = "domingo"
    return res

def dias_mas_combo(partidas:list[Partida])->str:
    aux = defaultdict(int)
    for i in partidas:
        if i.combo_finish:
            aux[i.fecha_hora.isoweekday()]+=1
    return cambiar_fecha(max(aux.items(), key = lambda x:x[1])[0])