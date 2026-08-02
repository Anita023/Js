import re

# ---------------- VALIDACIONES ---------------- #

def validate_document():
    while True:
        document = input("Número de documento: ").strip()

        if not document:
            display_message({"type": "error", "text": "El documento es obligatorio."})
            continue

        if not document.isdigit():
            display_message({"type": "error", "text": "El documento solo debe contener números."})
            continue

        if len(document) < 6 or len(document) > 10:
            display_message({"type": "error", "text": "El documento debe tener entre 6 y 10 dígitos."})
            continue

        return int(document)


def validate_document_type():
    while True:
        type_doc = input("Tipo de documento (CC/TI/CE): ").strip().upper()

        if type_doc not in ["CC", "TI", "CE"]:
            display_message({"type": "error", "text": "Solo se permite CC, TI o CE."})
            continue

        return type_doc


def validate_name():
    while True:
        name = input("Nombre completo: ").strip().title()

        if not name:
            display_message({"type": "error", "text": "El nombre es obligatorio."})
            continue

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", name):
            display_message({"type": "error", "text": "El nombre solo puede contener letras."})
            continue

        return name


def validate_group():
    while True:
        group = input("Número de ficha: ").strip()

        if not group.isdigit():
            display_message({"type": "error", "text": "La ficha solo debe contener números."})
            continue

        return group


def validate_program():
    while True:
        program = input("Programa de Formación: ").strip().title()

        if not program:
            display_message({"type": "error", "text": "El programa es obligatorio."})
            continue

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", program):
            display_message({"type": "error", "text": "El programa solo puede contener letras."})
            continue

        return program


def validate_email():
    while True:
        email = input("Correo electrónico: ").strip().lower()

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(pattern, email):
            display_message({"type": "error", "text": "Correo electrónico inválido."})
            continue

        return email


# ---------------- ENTRADA ---------------- #

def get_trainee_input():
    """Solicita al usuario los datos de un aprendiz."""

    return {
        "tipo_doc": validate_document_type(),
        "documento": validate_document(),
        "nombre": validate_name(),
        "correo": validate_email(),
        "ficha": validate_group(),
        "programa": validate_program()
    }


# ---------------- MENSAJES ---------------- #

def display_message(message):
    icons = {
        "success": "✅",
        "error": "❌",
        "info": "ℹ️"
    }

    print(f"{icons.get(message['type'],'')} {message['text']}")


def display_trainee_list(trainees):

    if not trainees:
        print("\nNo hay aprendices registrados.")
        return

    print("\n=========== APRENDICES ===========")

    for trainee in trainees:

        print(f"""
Documento : {trainee['documento']}
Tipo Doc  : {trainee['tipo_doc']}
Nombre    : {trainee['nombre']}
Correo    : {trainee['correo']}
Ficha     : {trainee['ficha']}
Programa  : {trainee['programa']}
----------------------------------------
""")


def display_confirm_next():

    display_message({
        "type": "info",
        "text": "¿Deseas registrar otro aprendiz? (s/n)"
    })

    option = input("> ").strip().lower()

    return option == "s"