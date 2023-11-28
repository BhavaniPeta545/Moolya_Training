import json
import random
from urllib.parse import urljoin

import requests
import jsonpath

class SimpleBooks:
    baseurl = "https://simple-books-api.glitch.me"
    def authenticate(self):
        global token
        baseurl = "https://simple-books-api.glitch.me"
        resource="/api-clients/"
        with open("authenticate.json",'r') as bdy:
            readbdy=bdy.read()
            postbody=json.loads(readbdy)
       #  num=str(random.randint(0,100))
       #  postbody={
       # "clientName": "Postman",
       # "clientEmail": "valentin" + num + "@example.com"
       #   }
        print(postbody)
        response=requests.post(urljoin(self.baseurl,resource),json=postbody)
        print(response.status_code)
        res=json.loads(response.text)
        token=jsonpath.jsonpath(res,'accessToken')
        print(token)
        return token

    def submit_order(self):
        print("======submit order=====")
        global id
        # num=random.randint(0,100)
        submit_resource=" /orders"
        print(token[0])
        auth_header={'Authorization': 'Bearer '+ token[0]}
        with open("submitboard.json", 'r') as bdy:
            readbdy = bdy.read()
            postbody = json.loads(readbdy)
        response=requests.post(urljoin(self.baseurl,submit_resource),json=postbody,headers=auth_header)
        print("submit order respnse code",response.status_code)
        res=json.loads(response.text)
        id=jsonpath.jsonpath(res,'orderId')
        print(id[0])
        return id[0]

    def get_orders(self):
        print("======get order=====")
        global id
        book_resource="/orders"
        auth_header = {'Authorization': 'Bearer ' + token[0]}
        response=requests.get(urljoin(self.baseurl,book_resource),headers=auth_header)
        print("get order response code", response.status_code)
        res = json.loads(response.text)
        print("orders are " ,res)
        # order_id = jsonpath.jsonpath(res, 'orderId')
        # print("order_id is  "+ order_id )
        # return order_id

    def update_order(self):
        print("====update order=====")
        update_resource='/orders/'+id[0]
        with open("update.json", 'r') as bdy:
            readbdy = bdy.read()
            update_body = json.loads(readbdy)
        auth_header = {'Authorization': 'Bearer ' + token[0]}
        response = requests.patch(urljoin(self.baseurl, update_resource),json=update_body,headers=auth_header)
        print("get update response code", response.status_code)
        # res = json.loads(response.text)
        # print("updated order is ", res)

    def delete_order(self):
        print("=====delete order====")
        delete_resource = '/orders/' + id[0]
        auth_header = {'Authorization': 'Bearer ' + token[0]}
        response = requests.delete(urljoin(self.baseurl, delete_resource),headers=auth_header)
        print("get delete response code", response.status_code)



c=SimpleBooks()
c.authenticate()
c.submit_order()
c.get_orders()
c.update_order()
c.delete_order()




