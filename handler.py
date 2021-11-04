import json
from compute import get_salary

def salary_extraction(event, context):
    text = event.get('text', None)
    
    if not text or text.strip() == '':
        message = {"message": "Enter valid text parameter"}
        return {'statusCode': 400, "body": json.dumps(message)}

    salary_str = get_salary(text)
    result = {"result": salary_str}
    return {"statusCode": 200, "body": json.dumps(result)}
