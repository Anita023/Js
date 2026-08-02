from models import trainee_model
from templates import trainee_template


def init_app_data():
    """
    Inicializa los datos de la aplicación.
    """
    trainee_model.load_data()


def register_trainee_view():
    """
    Registra un aprendiz.
    """

    # Solicitar información
    data = trainee_template.get_trainee_input()

    # Verificar si ya existe
    if trainee_model.search_by_document(data["documento"]):

        trainee_template.display_message(
            {
                "type": "error",
                "text": "Ya existe un aprendiz con ese número de documento."
            }
        )

        return

    # Registrar aprendiz
    trainee_model.register_trainee(data)

    trainee_template.display_message(
        {
            "type": "success",
            "text": f"El aprendiz {data['nombre']} fue registrado correctamente."
        }
    )



def edit_trainee_view():
    """
    Permite editar un aprendiz existente.
    """

    print("\n===== EDITAR APRENDIZ =====")

    document = trainee_template.validate_document()

    trainee = trainee_model.search_by_document(document)

    if not trainee:

        trainee_template.display_message({
            "type": "error",
            "text": "No existe un aprendiz con ese documento."
        })

        return

    updated_data = trainee_template.get_updated_trainee_input(trainee)

    trainee_model.update_trainee(document, updated_data)

    trainee_template.display_message({
        "type": "success",
        "text": f"El aprendiz {updated_data['nombre']} fue actualizado correctamente."
    })


def delete_trainee_view():
    """
    Elimina un aprendiz existente.
    """

    print("\n===== ELIMINAR APRENDIZ =====")

    document = trainee_template.validate_document()

    trainee = trainee_model.search_by_document(document)

    if not trainee:

        trainee_template.display_message({
            "type": "error",
            "text": "No existe un aprendiz con ese documento."
        })

        return

    trainee_model.delete_trainee(document)

    trainee_template.display_message({
        "type": "success",
        "text": f"El aprendiz {trainee['nombre']} fue eliminado correctamente."
    })

    
def status_view():
    """
    Muestra todos los aprendices.
    """

    trainees = trainee_model.get_all()

    trainee_template.display_trainee_list(trainees)