def gas_stations(distance, tank_size, stations):
    stations_list = []
    full_tank = tank_size
    burgas = stations[1:]
    burgas.append(distance)
    
    for i in range(len(stations)):
        if full_tank - stations[i] < stations[i] - burgas[i]:
            stations_list.append(stations[i])
            full_tank = tank_size
        else:
            full_tank -= stations[i]
    return stations_list
        




print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [80, 140, 220, 290]
gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) == [70, 140, 210, 280, 350]