import requests
response = request.get('https://api.github.com/user/ooctocat')

if response.status_code == 200:
    user_data = response.json()

    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Followers: {user_data['Followers']}")
    print(f"Following: {user_data['following']}")
else:
    print("Failed to retrieve data.")