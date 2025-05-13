import requests
import json

# Endpoint base da API GET (ajuste se necessário)
url = "https://app.way-v.com/api/integration/checklists"

# Parâmetros de query
params = {
    "execution_company_id": "6698fd4ade1b2a07d04c4a9f",
    "template_id": "67e5433420afa7d75cd70e37"
}

# Cabeçalhos com autenticação JWT
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55X2lkIjoiNjY5OGZkNGFkZTFiMmEwN2QwNGM0YTlmIiwiY3VycmVudF90aW1lIjoxNzQ0MzA1MTY4NzUzLCJleHAiOjIwNTk4Mzc5Njh9.ZU2yT2Ig5rYZ1VUt2N0ReBiB_0Ro-lADCUSXN-aoPjs",
    "Content-Type": "application/json"
}

# Requisição GET
response = requests.get(url, headers=headers, params=params)

# Verificando resposta
if response.status_code == 200:
    print("✅ Dados retornados com sucesso:")
    for item in response.json():
        # Formatting each dictionary item with line breaks
        print("--------- Item ---------")
        for key, value in item.items():
            # Handle nested dictionaries/lists with proper indentation
            if isinstance(value, (dict, list)):
                print(f"{key}:")
                # Using json.dumps with indent for nested structures
                formatted_value = json.dumps(value, indent=2, ensure_ascii=False)
                # Add indentation to each line of the formatted value
                indented_value = "\n".join(f"  {line}" for line in formatted_value.split("\n"))
                print(indented_value)
            else:
                print(f"{key}: {value}")
        print("\n")  # Extra line break between items
else:
    print(f"❌ Erro {response.status_code}")
    print(response.text)