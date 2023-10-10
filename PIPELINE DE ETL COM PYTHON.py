import pandas as pd
import requests
import openai

# Configuração da API do OpenAI
openai.api_key = 'ElfaTerrorista'  

def read_user_ids_from_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        return df['UserID'].tolist()
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {csv_file}')
        return []

def get_client_data(user_id):
    url = f'https://sdw-2023-prd.up.railway.app/users/{user_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro ao obter dados do cliente para o usuário {user_id}: {e}')
        return None

def generate_personalized_message_gpt4(client_data):
    message = ""

def update_news_for_user(user_id, personalized_message):
    put_url = f'https://sdw-2023-prd.up.railway.app/users/{user_id}'
    payload = {'news': personalized_message}

    try:
        response = requests.put(put_url, json=payload)
        response.raise_for_status()
        print(f'Mensagem atualizada para o usuário {user_id}')
    except requests.exceptions.RequestException as e:
        print(f'Falha ao atualizar a mensagem para o usuário {user_id}: {e}')

if __name__ == "__main__":
    csv_file = 'SDW2023.csv'
    user_ids = read_user_ids_from_csv(csv_file)

    for user_id in user_ids:
        client_data = get_client_data(user_id)

        if client_data:
            personalized_message = generate_personalized_message_gpt4(client_data)
            update_news_for_user(user_id, personalized_message)


