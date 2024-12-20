# coding:utf-8
import requests
import json

url = 'http://127.0.0.1/v1/chat-messages'
headers = {
    'Authorization': 'Bearer app-hdRypTioDgSS7QusctailImm',
    'Content-Type': 'application/json',
}
data = {
    "inputs": {},
    "query": "What are the specs of the iPhone 13 Pro Max?",
    "response_mode": "streaming",
    "conversation_id": "",
    "user": "baopanpan"
}

response = requests.post(url, headers=headers, data=json.dumps(data))
data_list = response.content.decode('utf-8').split('\n\n')
for data in data_list:
    if len(data) > 0:
        """
        {'event': 'message', 'conversation_id': 'aa55cf1b-b86d-40ae-b552-1987e456e569', 
        'message_id': '18a4d39e-b3f4-422b-9160-7897859f49b0', 'created_at': 1724402127, 
        'task_id': '8a0b439c-558e-483f-8096-3ae1defbd96f', 'id': '18a4d39e-b3f4-422b-9160-7897859f49b0', 'answer': ' some'}
        """
        data_dict = eval(data.split('data: ')[1])

with open('inshop_order_info_sql.txt', 'r') as file:
    file.read()


