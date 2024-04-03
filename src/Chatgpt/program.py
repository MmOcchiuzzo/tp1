# Importamos la librería OpenAI
import openai

# Configuramos la API Key de OpenAI
openai.api_key = 'tu_api_key_aqui'

# Definimos la función para procesar la consulta del usuario
def procesar_consulta(context, usertask, userquery):
    # Verificamos si la consulta del usuario tiene texto
    if userquery.strip() == '':
        print("Error: La consulta del usuario está vacía.")
        return

    # Creamos la solicitud para OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": usertask},
            {"role": "user", "content": userquery}
        ],
        temperature=1,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Imprimimos la respuesta de OpenAI
    print(response['choices'][0]['message']['content'])

