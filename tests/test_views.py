import sys
import os

# ESTO DEBE IR OBLIGATORIAMENTE EN LA LÍNEA 4 (antes de importar 'views')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# A partir de aquí van tus importaciones:
import pytest
from unittest.mock import patch

from src.views import trainee_view


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Fixture que se ejecuta automáticamente antes de cada prueba."""
    yield


# --- PRUEBA 1: Registro Exitoso ---
@patch("src.templates.trainee_template.display_message")
@patch("src.templates.trainee_template.get_trainee_input")
@patch("src.models.trainee_model.register_trainee")
@patch("src.models.trainee_model.search_by_document")


def test_register_trainee_view_success(
    mock_search, mock_register, mock_get_input, mock_display_msg
):
    mock_input_data = {
        "tipo_doc": "CC",
        "documento": "12345",
        "nombre": "Juan Perez",
        "ficha": "2671234",
        "programa": "ADSO",
        "email": "juan@sena.edu.co",
    }
    mock_get_input.return_value = mock_input_data
    mock_search.return_value = None

    trainee_view.register_trainee_view()

    mock_search.assert_called_once_with("12345")
    mock_register.assert_called_once_with(mock_input_data)
    mock_display_msg.assert_called_once_with(
        {
            "type": "success",
            "text": "El aprendiz Juan Perez fue registrado correctamente.",
        }
    )


# --- PRUEBA 2: Registro Duplicado ---
@patch("src.templates.trainee_template.display_message")
@patch("src.templates.trainee_template.get_trainee_input")
@patch("src.models.trainee_model.register_trainee")
@patch("src.models.trainee_model.search_by_document")


def test_register_trainee_view_duplicate(
    mock_search, mock_register, mock_get_input, mock_display_msg
):
    mock_input_data = {
        "tipo_doc": "CC",
        "documento": "12345",
        "nombre": "Juan Perez",
        "ficha": "2671234",
        "programa": "ADSO",
        "email": "juan@sena.edu.co",
    }
    mock_get_input.return_value = mock_input_data
    mock_search.return_value = mock_input_data

    trainee_view.register_trainee_view()

    mock_search.assert_called_once_with("12345")
    mock_register.assert_not_called()
    mock_display_msg.assert_called_once_with(
        {
            "type": "error",
            "text": "Ya existe un aprendiz con ese número de documento.",
        }
    )


# --- PRUEBA 3: Listado de Aprendices ---
@patch("src.templates.trainee_template.display_trainee_list")
@patch("src.models.trainee_model.get_all")


def test_status_view(mock_get_all, mock_display_list):
    mock_trainees = [
        {"documento": "123", "nombre": "Ana"},
        {"documento": "456", "nombre": "Carlos"},
    ]

    mock_get_all.return_value = mock_trainees

    trainee_view.status_view()

    mock_get_all.assert_called_once()
    mock_display_list.assert_called_once_with(mock_trainees)