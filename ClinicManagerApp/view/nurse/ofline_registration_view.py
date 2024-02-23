from flask_admin import expose
from flask_login import current_user
from flask import redirect, request, url_for
from ClinicManagerApp import app
from ClinicManagerApp.view.base_view import BaseView
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.controller.nurse.offline_registration_controller import \
    add_customer_daily, add_customer_db, get_remaining_amount_daily_slot, get_customer_daily_list
from ClinicManagerApp.controller.utils_controller import readJsonFile, writeJsonFile


class OfflineRegistrationView(BaseView):
    add_customer_result = None

    @expose('/')
    def index(self):
        return self.render('nurse/offline_registration.html',
                           amount=get_remaining_amount_daily_slot(),
                           add_customer_result=get_add_customer_result(),
                           daily_customer_list=get_customer_daily_list())


    def is_accessible(self):
        return current_user.is_authenticated and \
               current_user.role.name.lower().__contains__('y tá')


def get_add_customer_result():
    result = OfflineRegistrationView.add_customer_result
    OfflineRegistrationView.add_customer_result = None
    return result


def add_customer(customer=None):
    daily_customer_list = readJsonFile('daily_customer_list.json')
    OfflineRegistrationView.add_customer_result = add_customer_daily(id_card=customer.id_card)
    if OfflineRegistrationView.add_customer_result:
        OfflineRegistrationView.add_customer_result = add_customer_db(customer=customer)
        if not OfflineRegistrationView.add_customer_result:
            writeJsonFile(filename='daily_customer_list.json', data=daily_customer_list)


@app.route('/api/nurse/customer_offline_data', methods=['post'])
def get_data_offline_registration():
    id_card = request.form['id_card']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    sex = request.form['sex']
    date_of_birth = request.form['date_of_birth']
    email = request.form['email']
    address = request.form['address']
    phone_number = request.form['phone_number']
    customer = CustomerModel(id_card=id_card, first_name=first_name, last_name=last_name,
                             sex=sex.upper(), date_of_birth=date_of_birth, address=address,
                             phone_number=phone_number, email=email)
    add_customer(customer=customer)
    return redirect(url_for('offlineregistrationview.index'))
