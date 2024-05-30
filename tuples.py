def get_coordinate(record):
    tesoro, coordenada = record   
    return coordenada 
    
def convert_coordinate(coordinate):
    numero, letra = coordinate
    return numero, letra

def create_record(azara_record, rui_record):
    tesoro, coordenada = azara_record
    ubicación, coordenada, cuadrante = rui_record
    if  convert_coordinate(azara_record[1]) == rui_record[1]:
        return azara_record + rui_record
    else:
        return "not a match"
