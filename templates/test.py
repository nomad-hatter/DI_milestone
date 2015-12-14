import requests
r=requests.get('https://www.quandl.com/api/v3/datasets/WIKI/FB.json')
r.json()