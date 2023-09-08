import requests

url = "http://172.25.51.1/content.php"

payload = """
<params>
	<POST_VALUE_1>AAAAA</POST_VALUE_1>
	<POST_VALUE_2>BBBBB</POST_VALUE_2>
</params>
"""

my_header = {
	"Content-Type": "application/xml",
}

response = requests.post(url, data=payload, headers=my_header)

print(response.text)
