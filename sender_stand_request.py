import configuration
import requests
import data  # si ya tienes un archivo data.py con los datos del usuario

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # URL completa
                         json=body)  # Envía el cuerpo del request en formato JSON


def positive_assert(first_name):
    # Copiamos los datos base del archivo data.py
    user_body = data.user_body.copy()
    user_body["firstName"] = first_name  # Reemplazamos el nombre con el valor de prueba

    # Hacemos la solicitud POST
    response = post_new_user(user_body)

    # Verificamos el resultado esperado
    assert response.status_code == 201  # Código esperado
    assert response.json()["firstName"] == first_name  # Confirmamos que el nombre devuelto sea el mismo

