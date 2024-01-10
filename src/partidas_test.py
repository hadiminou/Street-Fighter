from partidas import*

def test_lee_partidas(datos:list[Partida]):
    print("\n1.test_lee_partidas")
    print(f"total de registros leidos: {len(datos)}")
    print(f"los tres primeros: {datos[:3]}")

def test_victoria_mas_rapida(datos:list[Partida]):
    print("\n2.test_victoria_mas_rapida")
    print(f"La partida mas rapida fue una entre {victoria_mas_rapida(datos)[0]} y \
        {victoria_mas_rapida(datos)[1]} que duro {victoria_mas_rapida(datos)[2]} segundos.")

def test_top_ratio_media_personajes(datos:list[Partida]):
    print("\n3.test_top_ratio_media_personajes")
    n = 3
    print(f"El top {n} de ratios medias es: {top_ratio_media_personajes(datos, n)}")

def test_enemigos_mas_debiles(datos:list[Partida]):
    print("\n4.test_enemigos_mas_debiles")
    print(enemigos_mas_debiles(datos, "Ken"))

def test_movimientos_comunes(datos:list[Partida]):
    print("\n5.test_movimientos_comunes")
    personaje1 = "Ryu"
    personaje2 = "Ken"
    print(f"Los movimientos repetidos entre {personaje1} y {personaje2} \
        son:{movimientos_comunes(datos, personaje1, personaje2)}")

def test_dias_mas_combo(datos:list[Partida]):
    print("\n6.test_dias_mas_combo")
    print(f"El dia que mas Ultra Combo Finish ha habido es el {dias_mas_combo(datos)}")

if __name__ == "__main__":
    datos = lee_partidas("data\games.csv")
    test_lee_partidas(datos)
    test_victoria_mas_rapida(datos)
    test_top_ratio_media_personajes(datos)
    test_enemigos_mas_debiles(datos)
    test_movimientos_comunes(datos)
    test_dias_mas_combo(datos)