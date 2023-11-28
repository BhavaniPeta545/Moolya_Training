import json
import random
from urllib.parse import urljoin
import jsonpath
import requests

baseurl = "https://simple-books-api.glitch.me"
authentication= "/api-clients/"
order_resource="/orders/"
num=str(random.randint(100,200))
booknum=str(random.randint(1,5))
# num=set(random.randrange(0,30))

auth={
    "clientName": "Postman" +num+ "nae",
    "clientEmail": "valentin"+num+"@example.com"
}
submit_book={
    "bookId": booknum,
    "customerName": "bhavani"+num
}
update_book={
  "customerName": "John5"
}
class Methods:

    def post_request(self,url,resource,json_data):
        return requests.post(urljoin(url,resource),json=json_data)

    def post_request_with_header(self,url,resource,json_data, header):
        return requests.post(urljoin(url,resource),json=json_data,headers=header)

    def get_request(self,url,resource,header):
        return requests.get(urljoin(url,resource),headers=header)

    def update_request(self,url,resource,json_data,header):
        return requests.patch(urljoin(url, resource), json=json_data, headers=header)

    def delete_request(self,url,resource,header):
        return requests.delete(urljoin(url, resource),headers=header)

    def fetch_data(self,response,data):
        res = json.loads(response.text)
        return jsonpath.jsonpath(res, data)



