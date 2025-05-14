def cria_form():
    url = "https://app.way-v.com/api/integration/checklists"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55X2lkIjoiNjY5OGZkNGFkZTFiMmEwN2QwNGM0YTlmIiwiY3VycmVudF90aW1lIjoxNzQ0MzA1MTY4NzUzLCJleHAiOjIwNTk4Mzc5Njh9.ZU2yT2Ig5rYZ1VUt2N0ReBiB_0Ro-lADCUSXN-aoPjs"


    # Configuração dos headers com o token de integração
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "checklist": {
            "template_id": "67e5433420afa7d75cd70e37",
            "execution_company_id": "6698fd4ade1b2a07d04c4a9f",
            "questions": [
                {"id": "bac4b5e1dfda4f82a6cac8f8083d3024", "sub_questions": [{"id": "1", "value":"33.333.33/0001-3"}]},
                {"id": "0d3378f02cfe41f6857532372b4dcb7a", "sub_questions": [{"id": "1", "value":"PontoPe"}]},

            ]
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(response)
        return True
    except Exception as e:
        print("\n")
        print(e)

        return False

cria_form()