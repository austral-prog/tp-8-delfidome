def get_coordinate(record):
    tesoro, coordenada = record
    return coordenada


def convert_coordinate(coordinate):
    num1 = coordinate[0]
    num2 = coordinate[1]
    return (num1, num2)


def create_record(azara_record, rui_record):
    treasure, coordinate1 = azara_record
    location, coordinate2, quadrant = rui_record

    if coordinate1[0] != coordinate2[0] or coordinate1[1] != coordinate2[1]:
        return "not a match"

    return (treasure,coordinate1, location, coordinate2, quadrant)
