import requests
def busca(): 
    request= requests.get('https://reqres.in/api/users')
    print(request.content)
print("Exibiu")
busca()