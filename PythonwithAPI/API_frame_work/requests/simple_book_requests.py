from API_frame_work.request_methods.api_methods import Rest_api_methods
from random import randint

from API_frame_work.request_methods.json_body import auth, submit_book


class Test_Simple_books(Rest_api_methods):
    Rest_api_methods.base_url = r'https://simple-books-api.glitch.me'
    json_test_file = r"../Data_retrieve/test_data.json"
    def Test_getting_access_token(self):
        token_data = self.post_requests(r"/api-clients/", auth)
        self.json_tets_data_returning(self.json_test_file,token_data.json())

    def Test_create_order(self):
        json_file_data = self.json_data_retrieving(self.json_test_file)
        response = self.post_requests(r"/orders/", submit_book, json_file_data['accessToken'])
        json_file_data.update(id=response.json()['orderId'])
        self.json_tets_data_returning(self.json_test_file, json_file_data)
        print(response.json())

    def Test_get_book(self):
        order_id = self.json_data_retrieving(self.json_test_file)['id']
        end_point = fr"/orders/{order_id}"
        json_file_data = self.json_data_retrieving(self.json_test_file)
        res = self.get_request(end_point, json_file_data['accessToken'])
        print(res.json())
        return res

    def deleting_a_book(self):
        json_file_data = self.json_data_retrieving(self.json_test_file)
        order_id = self.json_data_retrieving(self.json_test_file)['id']
        end_point = fr"/orders/{order_id}"
        response = self.delete_request(end_point, json_file_data['accessToken'])
        print(response)
        print(self.Test_get_book())


a = Test_Simple_books()
a.Test_getting_access_token()
a.Test_create_order()
a.Test_get_book()
a.deleting_a_book()