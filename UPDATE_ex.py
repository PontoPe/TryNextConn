def altera_cadastro_aluno(url, _id, key1, value1, key2,value2):
    global Lista_erros
    perc_presenca= 0

    if value1 is not None and value2 is not None:
        try:
            value1_float = float(value1)
            value2_float = float(value2)
            perc_presenca = (value2_float / value1_float) * 100
            perc_presenca = round(perc_presenca, 2)
        except ValueError:
            print(f"ValueError: Não foi possível converter value1 ({value1}) ou value2 ({value2}) para float.")
    else:
        #print(f"Valores inválidos: value1 = {value1}, value2 = {value2}")
        perc_presenca = 0
    key3 = "b3deacb482a8490ab174d112e8b27810"
    key4 = "ff944f56fbc94f7cbd4f92ae71af1417"
    payload = {
        "checklist": {
            "id": _id,
            "questions": [
                {
                    "id": key1,
                    "sub_questions": [
                        {
                            "id": "1",
                            "value": value1
                        }
                    ]
                },
                {
                    "id": key2,
                    "sub_questions": [
                        {
                            "id": "1",
                            "value": value2
                        }
                    ]
                },
                {
                    "id": key3,
                    "sub_questions": [
                        {
                            "id": "1",
                            "value": str(perc_presenca)
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, json=payload, headers=headers)