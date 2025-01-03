# # Данные массивы
# first_array = ['00761592', '00761588', '00761591', '00761589', '00761593', '00125', '00761590', '00762173', '00761266', '00761259', '00761295']
# second_array = ['00761588', 9, '00761589', 7, '00761590', 10, '00761593', 10, '00761592', 10, '00761591', 10, '00125', 8, '00761266', 10, '00761295', 10, '00761259', 9, '00762173', 30]
# third_array = ['00761588', 52, '00761589', 54, '00761590', 1, '00761593', 0, '00761592', 38, '00761591', 44, '00125', 83, '00761266', 9, '00761295', 5, '00761259', 0, '00762173', 35]

# # Результирующий массив, содержащий соответствующие значения
# result = []

# # Проходим по первому массиву
# for offer_id in first_array:
#     # Находим соответствующие значения во втором и третьем массиве
#     second_value = None
#     third_value = None
    
#     # Поиск вэ втором массиве
#     for i in range(0, len(second_array), 2):
#         if second_array[i] == offer_id:
#             second_value = second_array[i + 1]
#             break

#     # Поиск в третьем массиве
#     for i in range(0, len(third_array), 2):
#         if third_array[i] == offer_id:
#             third_value = third_array[i + 1]
#             break

#     # Добавляем к результату кортеж из offer_id, второго и третьего значений
#     result.append((offer_id, second_value, third_value))

# # Выводим результат
# for item in result:
#     print(item)


import sys
import json
import requests

from des import *
from math import *
from tabulate import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.showFullScreen()   
        self.ui.plainTextEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)


        self.ui.pushButton.clicked.connect(self.v3_posting_fbs_list) 
        self.ui.pushButton_2.clicked.connect(self.v2_posting_fbo_list) 


    def v2_posting_fbo_list(self):


        url = 'https://api-seller.ozon.ru/v2/posting/fbo/list'

        headers = {
            'Client-Id': '1898519',
            'Api-Key': '7441b4a6-0424-48a3-bb95-f28a20e678a2',
            # 'Client-Id': str(self.ui.client_id.text()),
            # 'Api-Key': str(self.ui.api_key.text() ),
        }

        jjson = {
        "dir": "ASC",
        "filter": {
            "since": "2023-09-01T00:00:00Z",
            "status": "",
            "to": "2024-08-01T00:00:00Z"
        },
        "limit": 1000,
        "offset": 0,
        "translit": False,
        "with": {
            "analytics_data": False,
            "financial_data": False
        }
        }

        response = requests.post(url, headers=headers, json=jjson)

        data = response.json()
        # print(json.dumps(data, indent=4, ensure_ascii=False))

        with open("main.json", "w") as f:
            d = {"my_key": data}
            json.dump(d, f, indent=4)

        f.close

        Name_Offer_id_H = d['my_key']['result']

        Name_Offer_id = []

        Offer_id = []


        for i in Name_Offer_id_H:
            if (i['products'][0]['name']) not in Name_Offer_id:
                Name_Offer_id.append(i['products'][0]['name']) 
                Name_Offer_id.append(i['products'][0]['offer_id'])
                Offer_id.append(i['products'][0]['offer_id'])

        print(Name_Offer_id)
        return Name_Offer_id, Offer_id


    def v3_product_info_stocks(self, id):
        url = 'https://api-seller.ozon.ru/v3/product/info/stocks'

        headers = {
            'Client-Id': '1898519',
            'Api-Key': '7441b4a6-0424-48a3-bb95-f28a20e678a2',
            # 'Client-Id': str(self.ui.client_id.text()),
            # 'Api-Key': str(self.ui.api_key.text() ),
        }
        jjson = {
        "filter": {
        "offer_id": id,
        "visibility": "ALL"},
        "last_id": "",
        "limit": 100
        }

        response = requests.post(url, headers=headers, json=jjson)

        self.data = response.json()
        # print(json.dumps(self.data, indent=4, ensure_ascii=False))

        with open("id.json", "w") as f:
            d = {"my_key": self.data}
            json.dump(d, f, indent=4)
        
        f.close
        


    def stocks_fbo_fbs(self):
        stocks_fbo_fbs_all, stocks_fbo_fbs_id = self.v2_posting_fbo_list()

        print(stocks_fbo_fbs_all)

        print(stocks_fbo_fbs_id)
        self.v3_product_info_stocks(id=stocks_fbo_fbs_id)


        
        with open("id.json", 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        # Массивы для хранения результатов
        fbs_array = []
        fbo_array = []

        # Проход по элементам в "items"
        for item in json_data['my_key']['result']['items']:
            for stock in item['stocks']:
                if stock['type'] == 'fbs':
                    fbs_array.append(item['offer_id'])
                    fbs_array.append(stock['present'])

                elif stock['type'] == 'fbo':
                    fbo_array.append(item['offer_id'])
                    fbo_array.append(stock['present'])

        print("Массив fbs:")
        print(fbs_array)
        print("\nМассив fbo:")
        print(fbo_array)


        first_array = stocks_fbo_fbs_id
        second_array = fbs_array
        third_array = fbo_array

        result_stocks_fbo_fbs = []

        for offer_id in first_array:
            second_value = None
            third_value = None
            
            for i in range(0, len(second_array), 2):
                if second_array[i] == offer_id:
                    second_value = second_array[i + 1]
                    break

            for i in range(0, len(third_array), 2):
                if third_array[i] == offer_id:
                    third_value = third_array[i + 1]
                    break

            result_stocks_fbo_fbs.append([offer_id, second_value, third_value])

        print(result_stocks_fbo_fbs)

        print(result_stocks_fbo_fbs[1][2])

        for item in result_stocks_fbo_fbs:
            print(item)

        return result_stocks_fbo_fbs




    def v3_posting_fbs_list(self):
        self.v2_posting_fbo_list()
        print(1111111111111111111111)
        self.stocks_fbo_fbs()
        print(2222222222222222222222)
        url = 'https://api-seller.ozon.ru/v3/posting/fbs/list'

        headers = {
            # 'Client-Id': '1898519',
            # 'Api-Key': '7441b4a6-0424-48a3-bb95-f28a20e678a2',
            'Client-Id': str(self.ui.client_id.text()),
            'Api-Key': str(self.ui.api_key.text() ),
        }

        v3_posting_fbs_list_json = {
        "dir": "ASC",
        "filter": {
            "delivery_method_id": [
            "1893206"
            ],
            # "since": '2024-07-01T00:00:00Z',
            # "to": '2024-08-01T00:00:00Z',
            # "warehouse_id": ['1020001804381000']
            "since": str(self.ui.data_from.text())+"T00:00:00Z",
            "to": str(self.ui.data_to.text())+"T00:00:00Z",
            "warehouse_id": [str(self.ui.warehouse_id.text())]
        },
        "limit": 1000,
        "offset": 0,
        "with": {
            "analytics_data": True,
            "barcodes": True,
            "financial_data": True,
            "translit": True
        }
        }




        response = requests.post(url, headers=headers, json=v3_posting_fbs_list_json)

        self.RRR = response.json()
        # print(json.dumps(self.RRR, indent=4, ensure_ascii=False))


        with open("main.json", "w") as f:
            d = {"my_key": self.RRR}
            json.dump(d, f, indent=4)
        
        f.close

        Product_Name_List_Postings = d['my_key']['result']['postings']

        Product_Name_List = []



        for i in Product_Name_List_Postings:
            Product_Name_List.append(i['products'][0]['name']) 
        
        # print(1111111111111111111111)
        # print(Product_Name_List)
        # print(1111111111111111111111)
        # result_stocks_fbo_fbs = self.stocks_fbo_fbs()


        self.pretty_print_json()


    def pretty_print_json(self):

        # result_stocks_fbo_fbs = self.stocks_fbo_fbs()

        with open("main.json", 'r') as f:
            data = json.load(f)

        postings = data['my_key']['result']['postings']

        headers = [
            '№', 'Posting Number', 'Order ID', 'Order Number', 'Status', 'Delivery Method', 'Tracking Number',
            'Shipment Date', 'Delivering Date', 'Product Name', 'Price', 'Quantity', 'Region', 'City', 
            'Delivery Type', 'Payment Type', 'Warehouse', 'TPL Provider', 'Commission Amount', 'Payout'
        ]


        table_data = []
        for index, posting in enumerate(postings):
            row = []
            row.append(index + 1)  
            row.append(posting['posting_number'])
            row.append(posting['order_id'])
            row.append(posting['order_number'])
            row.append(posting['status'])
            row.append(posting['delivery_method']['name'])
            row.append(posting['tracking_number'])
            row.append(posting['shipment_date'])
            row.append(posting['delivering_date'])
            row.append(posting['products'][0]['name'])  
            row.append(posting['products'][0]['price'])
            row.append(posting['products'][0]['quantity'])
            row.append(posting['analytics_data']['region'])
            row.append(posting['analytics_data']['city'])
            row.append(posting['analytics_data']['delivery_type'])
            row.append(posting['analytics_data']['payment_type_group_name'])
            row.append(posting['analytics_data']['warehouse'])
            row.append(posting['analytics_data']['tpl_provider'])
            row.append(posting['financial_data']['products'][0]['commission_amount'])
            row.append(posting['financial_data']['products'][0]['payout'])

            table_data.append(row)

        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        tabl = (tabulate(table_data, headers=headers, tablefmt="grid"))
        
        self.ui.plainTextEdit_2.setPlainText('')

        self.ui.plainTextEdit_2.appendPlainText(tabl)


    # pretty_print_json("main.json") 


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())