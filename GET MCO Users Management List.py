import requests
f = open('output1.txt', 'w', encoding='utf-8' )
response = requests.get('https://webapi.teamviewer.com/api/v1/users' , headers={'Authorization': 'Bearer YOURTOKENHERE'})
f.write(response.text)
f.close()
