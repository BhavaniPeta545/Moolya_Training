import json
import random
from urllib.parse import urljoin

import requests
import jsonpath
from requests import post

from SimplebooksApi.authenticate import *


class SimpleBooks(Methods):

    def authenticate(self):
        global token
        print("======auth=======")
        response=Methods.post_request(self,baseurl,authentication,auth)
        print(response.status_code)
        token=Methods.fetch_data(self,response,'accessToken')
        print(token)

    def submit_order(self):
        print("======submit order=====")
        global id
        auth_header={'Authorization': 'Bearer '+ token[0]}
        print(token[0])
        response=Methods.post_request_with_header(self,baseurl,order_resource,submit_book,auth_header)
        print("submit order response code",response.status_code)
        id=Methods.fetch_data(self,response,'orderId')
        print(id)

    def get_orders(self):
        print("======get order=====")
        global id
        auth_header = {'Authorization': 'Bearer ' + token[0]}
        response=Methods.get_request(self,baseurl,order_resource,auth_header)
        print("get order response code", response.status_code)
        res = json.loads(response.text)
        print("orders are " ,res)
        # order_id = jsonpath.jsonpath(res, 'orderId')
        # print("order_id is  "+ order_id )
        # return order_id

    def update_order(self):
        print("====update order=====")
        update_resource='/orders/'+id[0]
        auth_header = {'Authorization': 'Bearer ' + token[0]}
        response = Methods.update_request(self,baseurl,update_resource,update_book,auth_header)
        print("get update response code", response.status_code)
        # res = json.loads(response.text)
        # print("updated order is ", res)

    def delete_order(self):
        print("=====delete order====")
        delete_resource = '/orders/' + id[0]
        auth_header = {'Authorization': 'Bearer ' + token[0]}
        response =Methods.delete_request(self,baseurl,delete_resource,auth_header)
        print("get delete response code", response.status_code)



c=SimpleBooks()
c.authenticate()
c.submit_order()
c.get_orders()
c.update_order()
c.delete_order()




