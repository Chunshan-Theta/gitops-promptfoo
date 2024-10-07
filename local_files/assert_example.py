import requests
import json
from typing import Dict, TypedDict, Union, Any

def get_assert(output: str, context) -> Union[bool, float, Dict[str, Any]]:
    input_content = output
    rubrics = context['test']['assert'][0]['config']['rubrics']

    ans = _call_answer_ai_api(input_content,rubrics)
    return {
      'pass': True if 'TRUE' in ans.upper() else False,
      'score': 1.0 if 'TRUE' in ans.upper() else 0.0,
      'reason': f"{ans}\n ans.upper() = `{ans.upper()}`",
    }
def _call_answer_ai_api(input_content, rubrics):
    url = "https://<host>/api/v1/chat/completions"

    payload = json.dumps({
    "chatId": "test-20241004-1",
    "stream": False,
    "detail": False,
    "messages": [
        {
        "content": """
            Rate <Input> according to the <Rubric>. If the <Input> passes the <Rubric>, the response is `TRUE`. Else if response `FALSE`.
            ###example###
            <Input>
            Hi there

            <Rubric>
            Contains greetings

            <Response>
            TRUE

            ###Important Note###
            - Please generate only the following JSON object without any additional text or commentary. The output should strictly match this format: `<Response> TRUE`.
            - If unsure, please respond with `FALSE`.
            - Only return <Response>,do not reply any explanatory or introductory text.
            """,
        "role": "user"
        },
        {
        "content": f"<Input>\n{input_content}\n<Rubric>\n{rubrics}\n<Response>\n",
        "role": "user"
        }
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer fastgpt-yFPnAMu6G76MAw3Z4oBPzyhtorfxD4DBZljKbIZ3kUkgxUUsr1HMuxiaTG'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['choices'][0]['message']['content']
