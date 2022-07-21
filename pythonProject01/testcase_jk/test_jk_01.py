import requests


class TestJK:
    def test_01_jk(self):
        test_url = "http://httpbin.org/get?"
        headers = {"test-Agent": "json"}
        test_data = {"one": 1, "two": 2}
        response = requests.request("GET", test_url, headers=headers, params=test_data)
        print(response.text)
