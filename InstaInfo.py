import requests
import json
import webbrowser

username = input("Instagram Username : ")

url = "https://easy-instagram-service.p.rapidapi.com/username"

querystring = {"username":username,"random":"x8n3nsj2"}

headers = {
	"X-RapidAPI-Host": "easy-instagram-service.p.rapidapi.com",
	"X-RapidAPI-Key": "YOUR KEY HERE"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.text

data = json.loads(data)

userid = data['id']
fullname = data['full_name']
profile_pic_url = data['profile_pic_url']
bio = data["biography"]
username = data['username']
is_private = data['is_private']
following = data['following']
follower = data['follower']
like = data['like']
comments = data['comment']
total_post = data['total_post']

all_data = f"""
<!DOCTYPE html>
<html>
<head>
<title>InstaInfo For {username} Profile</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>

<div class='container'>

<div  style="margin-top: 5em;" class="card mb-3">
  <img src="{profile_pic_url}" class="card-img-top" alt="{username} Profile Picture">
  <div class="card-body">
    <h5 class="card-title">[+] Fullname : {fullname}</h5>
    <p class="card-text">[+] User ID : {userid}</p>
    <p class="card-text">[+] Bio : {bio}</p>
    <p class="card-text">[+] Is Private Acc : {is_private}</p>
	<p class="card-text">[+] Following : {following}</p>
	<p class="card-text">[+] Follower : {follower}</p>
	<p class="card-text">[+] Like : {like}</p>
	<p class="card-text">[+] Comments : {comments}</p>
	<p class="card-text">[+] Total Posts : {total_post}</p>
	</div>
</div>
</div>
</body>
</html>
"""
print("Data Fetched !")

user = str(input("Save Data Into A HTML File (y or n) : "))

if user == "y" or "Y":
	save_file = open(f"{username}.html","w+")
	save_file.write(all_data)
	save_file.close
	print(f'[+] Files Saved At : {username}.html')
	
else:
    print("[+] Exit The Program !")

ask_user = str(input("Open File In Browser (y or n): "))

if ask_user == 'y' or "Y":

    webbrowser.open(f"{username}.html")

else:

	print("[+] Exit The Program !")
