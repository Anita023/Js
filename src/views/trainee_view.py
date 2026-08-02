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


def status_view():
    """
    Muestra todos los aprendices.
    """

    trainees = trainee_model.get_all()

    trainee_template.display_trainee_list(trainees)