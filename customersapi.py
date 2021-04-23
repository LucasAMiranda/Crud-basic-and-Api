from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime, date

app = Flask(__name__)
api = Api(app)

customers = []


class Customer(Resource):

    def get(self, id):
        for cust in customers:
            if cust['id'] == id:
                return {'data': cust}
            return {'data': None}

    def delete(self, id):
        for index, cust in enumerate(customers):
            if cust['id'] == id:
                customers.pop(index)
                return{'message': 'Deleted is successfully!'}
        return {'data': None}

    def put(self, id):
        request_data = request.get_json()
        for index, cust in enumerate(customers):
            if cust['id'] == id:
                cust = request_data
                customers[index] = cust
            return {'data': cust}
        return{'data': None}


class CustomerList(Resource):

    def get(self):
        return {'data': customers}

    def post(self):
        request_data = request.get_json()
        cust = {
            'id': len(customers) + 1,
            'name': request_data['name'],
            'birth_date': request_data['birth_date']
        }
        customers.append(cust)
        return {'data': cust}


api.add_resource(Customer, '/customers/<int:id>')
api.add_resource(CustomerList, '/customers')

if __name__ == '__main__':
    app.run(debug=True)
