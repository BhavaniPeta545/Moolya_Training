import requests
import json


class Rest_api_methods:
    base_url = ''

    # def pay_load_convert_json(self, body):
    #     pay_load = json.dumps(body)
    #     return pay_load

    def get_request(self, end_point, authentication=''):
        if not authentication:
            response = requests.get(self.base_url+end_point)
            return response
        elif authentication:
            Acc_token = {'Authorization': 'Bearer ' + authentication}
            response = requests.get(self.base_url+end_point, headers=Acc_token)
            return response


    def post_requests(self, end_point, body, authetication=''):
        if not authetication:
            response = requests.post(self.base_url+end_point,json=body)
            return response

        if authetication:
            Acc_token = {'Authorization': 'Bearer '+authetication}
            response = requests.post(self.base_url+end_point,json=body, headers=Acc_token)
            return response


    def delete_request(self, end_point, authentication=''):
        Acc_token = {'Authorization': 'Bearer ' + authentication}
        response = requests.delete(self.base_url+end_point, headers=Acc_token)


    def json_data_retrieving(self, file_name):
        with open(fr"{file_name}", 'r') as json_file2:
            data = json.load(json_file2)
            return data

    def json_tets_data_returning(self, file_name, data):
        with open(fr"{file_name}", 'w') as json_file1:
            json.dump(data, json_file1)


