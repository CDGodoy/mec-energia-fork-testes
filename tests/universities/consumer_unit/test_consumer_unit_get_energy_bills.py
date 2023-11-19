import json
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from datetime import date
import random

from tests.test_utils import dicts_test_utils
from tests.test_utils import create_objects_test_utils

from utils.energy_bill_util import EnergyBillUtils

ENDPOINT = '/api/consumer-units/'
EMAIL = 'admin@admin.com'
PASSWORD = 'admin@admin.com'

@pytest.mark.django_db
class TestConsumerUnitsProperties:
    def setup_method(self):
        self.university_dict = dicts_test_utils.university_dict_1
        self.user_dict = dicts_test_utils.university_user_dict_1

        self.university = create_objects_test_utils.create_test_university(self.university_dict)
        self.user = create_objects_test_utils.create_test_university_user(self.user_dict, self.university)
        
        self.client = APIClient()
        self.client.login(
            email = self.user_dict['email'], 
            password = self.user_dict['password'])

        self.distributor_dict = dicts_test_utils.distributor_dict_1
        self.distributor = create_objects_test_utils.create_test_distributor(self.distributor_dict, self.university)
        
        self.consumer_unit_test_1_dict = dicts_test_utils.consumer_unit_dict_1
        self.consumer_unit_test_1 = create_objects_test_utils.create_test_consumer_unit(self.consumer_unit_test_1_dict, self.university)

        self.consumer_unit_test_2_dict = dicts_test_utils.consumer_unit_dict_2
        self.consumer_unit_test_2 = create_objects_test_utils.create_test_consumer_unit(self.consumer_unit_test_2_dict, self.university)

        self.contract_test_1_dict = dicts_test_utils.contract_dict_1
        self.contract_test_1 = create_objects_test_utils.create_test_contract(self.contract_test_1_dict, self.distributor, self.consumer_unit_test_1)

        self.contract_test_2_dict = dicts_test_utils.contract_dict_2
        self.contract_test_2 = create_objects_test_utils.create_test_contract(self.contract_test_2_dict, self.distributor, self.consumer_unit_test_2)

        self.energy_bill_test_1_dict = dicts_test_utils.energy_bill_dict_1
        self.energy_bill_test_1 = create_objects_test_utils.create_test_energy_bill(self.energy_bill_test_1_dict, self.contract_test_2, self.consumer_unit_test_2)


    def test_get_energy_bills_by_year_year_less_than_consumer_unit_year(self):   
        with pytest.raises(Exception, match="Consumer User do not have Energy Bills this year"):
            self.consumer_unit_test_1.get_energy_bills_by_year(1999)

    def test_get_energy_bills_by_year_year_greater_than_today_year(self):   
        actual_year = date.today().year
        greater_year = actual_year + random.randint(1, 100)
        with pytest.raises(Exception, match="Consumer User do not have Energy Bills this year"):
            self.consumer_unit_test_1.get_energy_bills_by_year(greater_year)
    
    def test_get_energy_bills_by_year_right_year(self):   
        consumer_unit_test_2_year = self.consumer_unit_test_2.date.year
        energy_bills = self.consumer_unit_test_2.get_energy_bills_by_year(consumer_unit_test_2_year)
        assert len(energy_bills) == 12
        assert type(energy_bills) == list
        assert energy_bills[1]['energy_bill'] == EnergyBillUtils.energy_bill_dictionary(self.energy_bill_test_1)
