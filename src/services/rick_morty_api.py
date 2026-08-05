import random
import httpx

API_URL = "https://rickandmortyapi.com/api/character"


async def get_random_character(character_id: int = None):
    """
    Obtiene un personaje aleatorio o uno específico.
    """

    if character_id is None:
        character_id = random.randint(1, 826)

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{API_URL}/{character_id}",
                timeout=5.0
            )

            if response.status_code == 200:
                data = response.json()

                return {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "status": data.get("status"),
                    "species": data.get("species"),
                    "image": data.get("image")
                }

    except Exception:
        return None

    return None