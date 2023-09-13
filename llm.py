import requests
from socket_input import input_data

#! Output Function
def result(full=False):
    if(full):
        return response.json()
    else:
        return response.json()['BOT']




url = "https://open-ai21.p.rapidapi.com/conversationgpt35"

payload = {
	"messages": [
		{
			"role": "user",
			"content": input_data()
		}
	],
	"stream": False
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "d646f7e495mshb9c44148d6a8fdfp1a52ffjsn7c392d37ddc0",
	"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

# print(result())