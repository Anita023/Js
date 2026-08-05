from fastapi import FastAPI, HTTPException

from services.rick_morty_api import get_random_character

app = FastAPI(
    title="Rick and Morty Consumer API",
    description="API simple con FastAPI para consumir la API de Rick & Morty",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a la API de Rick & Morty con FastAPI. Visita /docs para ver la documentación interactiva."
    }


@app.get("/character/random")
async def read_random_character():

    character = await get_random_character()
from fastapi import FastAPI, HTTPException

from services.rick_morty_api import get_random_character

app = FastAPI(
    title="Rick and Morty Consumer API",
    description="API simple con FastAPI para consumir la API de Rick & Morty",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a la API de Rick & Morty con FastAPI. Visita /docs para ver la documentación interactiva."
    }


@app.get("/character/random")
async def read_random_character():
    """
    Endpoint para obtener un personaje aleatorio.
    """

    character = await get_random_character()

    if not character:
        raise HTTPException(
            status_code=500,
            detail="No se pudo obtener el personaje de la API externa."
        )

    return character


@app.get("/character/{character_id}")
async def read_character_by_id(character_id: int):
    """
    Endpoint para obtener un personaje por ID.
    """

    if character_id < 1 or character_id > 826:
        raise HTTPException(
            status_code=400,
            detail="El ID del personaje debe estar entre 1 y 826."
        )

    character = await get_random_character(character_id=character_id)

    if not character:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró el personaje con ID {character_id}."
        )

    return character
    if not character:
        raise HTTPException(
            status_code=500,
            detail="No se pudo obtener el personaje de la API externa."
        )

    return character


@app.get("/character/{character_id}")
async def read_character_by_id(character_id: int):

    if character_id < 1 or character_id > 826:
        raise HTTPException(
            status_code=400,
            detail="El ID del personaje debe estar entre 1 y 826."
        )

    character = await get_random_character(character_id=character_id)

    if not character:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró el personaje con ID {character_id}."
        )

    return character