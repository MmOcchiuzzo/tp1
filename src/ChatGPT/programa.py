import openai
import readline
import sys

buffer = []
last_query = ""

def procesar_consulta(context, usertask, userquery):
    global last_query, buffer
    
    try:
        
        if userquery.strip() == '':
            raise ValueError("La consulta del usuario está vacía.")
        last_query = userquery
        buffer.append(userquery)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": usertask},
                {"role": "user", "content": last_query}
            ],
            temperature=1,
            max_tokens=4096,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        answer = response['choices'][0]['message']['content']
        
        buffer.append(answer)

        print(answer)
    
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error al procesar la consulta:", e)

def input_with_history(prompt):
    readline.set_history_length(100) 
    readline.parse_and_bind('"\e[A": history-search-backward') 
    
    try:
        line = input(prompt)
        return line
    except (KeyboardInterrupt, EOFError):
        print("\nSaliendo del programa...")
        exit()

if len(sys.argv) > 1 and sys.argv[1] == "--convers":
    print("Modo conversación activado.")
    print("Puede ingresar consultas ('exit' para salir).")

    try:
        while True:
            userquery = input_with_history("Ingrese su consulta: ")

            if userquery.lower() == 'exit':
                break 
            
            procesar_consulta("Contexto inicial", "Tarea del usuario", userquery)
        
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        exit()

else:
    print("Modo conversación no activado. Use el argumento '--convers' para activar este modo.")

