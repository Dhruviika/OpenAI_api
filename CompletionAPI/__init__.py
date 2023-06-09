import logging
import openai
import azure.functions as func

openai.api_key = 'your_api_key'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    

    req_body = req.get_json()
    logging.info(type(req_body))

    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    )

    output_text = output['choices'][0]['text']
   
    return func.HttpResponse(output_text,status_code=200)
        
