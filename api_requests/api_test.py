# https://any-api.com/ - czytać i rejestrować się
# https://www.ipify.org/ - mamy za darmo od razu
# https://programujwzespole.edu.pl/ - projekt nauki pisania w Pythonie

import requests
import sys

url = "https://api.ipify.org?format=json"
try:
    data = requests.get(url)
except Exception as e:
    print(f"Error - {e}")
    sys.exit(2)

print(data)
if data.status_code == 200:
    ip_json = data.json()
    print(f"Your public IP is raw: {ip_json['ip']}")
else:
    print(f"Error - {data.status_code}")
