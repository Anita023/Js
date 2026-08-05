import json
import os
import csv

# Ruta absoluta del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta data
DATA_DIR = os.path.join(BASE_DIR, "data")

# Archivo JSON
DATABASE_FILE = os.path.join(DATA_DIR, "trainees.json")

trainees = []


def ensure_data_file_exists():
    """
    Crea la carpeta data y el archivo trainees.json
    si no existen.
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)


def load_data():
    """
    Carga los aprendices almacenados.
    """
    global trainees

    ensure_data_file_exists()

    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            trainees = json.load(file)
    except json.JSONDecodeError:
        trainees = []


def save_data():
    """
    Guarda la información en el archivo JSON.
    """
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(trainees, file, ensure_ascii=False, indent=4)


def get_all():
    return trainees


def search_by_document(document):
    """
    Busca un aprendiz por documento.
    """
    for trainee in trainees:
        if trainee["documento"] == document:
            return trainee
    return None


def register_trainee(new_trainee):
    """
    Registra un nuevo aprendiz.
    """
    if search_by_document(new_trainee["documento"]):
        return False

    trainees.append(new_trainee)
    save_data()
    return True


# =============================
# PUNTO 3 - EDITAR APRENDIZ
# =============================

def update_trainee(document, updated_data):
    """
    Actualiza la información de un aprendiz existente.
    """
    for index, trainee in enumerate(trainees):

        if trainee["documento"] == document:

            trainees[index] = updated_data

            save_data()

            return True

    return False


# =============================
# PUNTO 4 - ELIMINAR APRENDIZ
# =============================

def delete_trainee(document):
    """
    Elimina un aprendiz por su número de documento.
    """
    global trainees

    for trainee in trainees:
        if trainee["documento"] == document:
            trainees.remove(trainee)
            save_data()
            return True

    return False


# =============================
# PUNTO 5 - BUSCAR APRENDICES
# =============================

def search_by_name(name):
    """
    Busca aprendices por nombre.
    """
    results = []

    for trainee in trainees:
        if name.lower() in trainee["nombre"].lower():
            results.append(trainee)

    return results


def search_by_group(group):
    """
    Busca aprendices por número de ficha.
    """
    results = []

    for trainee in trainees:
        if trainee["ficha"] == group:
            results.append(trainee)

    return results



# =============================
# PUNTO 6 - EXPORTAR A CSV
# =============================

def export_to_csv():
    """
    Exporta la lista de aprendices a un archivo CSV.
    """

    csv_file = os.path.join(DATA_DIR, "trainees.csv")

    with open(csv_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "tipo_doc",
            "documento",
            "nombre",
            "email",
            "ficha",
            "programa"
        ])

        for trainee in trainees:

            writer.writerow([
                trainee["tipo_doc"],
                trainee["documento"],
                trainee["nombre"],
                trainee["email"],
                trainee["ficha"],
                trainee["programa"]
            ])

    return csv_file