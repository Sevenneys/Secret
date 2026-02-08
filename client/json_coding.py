import json

def run_json(*, state: int, value: dict) -> str:
    
    if state == 1:
        return json.dumps(value)
    elif state == 0:
        return json.loads(value)
    else:
        print(f"Неверное значение..\n\n1 - кодированние\n0 - декодированние")






