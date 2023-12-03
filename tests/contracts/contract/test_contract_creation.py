import pytest

from tests.test_utils import dicts_test_utils
from tests.test_utils import create_objects_test_utils
from datetime import date
from contracts.models import EnergyBill

@pytest.mark.django_db
class TestContractCreation:
    def setup_method(self):
        self.university_dict = dicts_test_utils.university_dict_1
        self.university = create_objects_test_utils.create_test_university(self.university_dict)

        self.distributor_dict = dicts_test_utils.distributor_dict_1
        self.distributor = create_objects_test_utils.create_test_distributor(self.distributor_dict, self.university)

        self.consumer_unit_test_dict = dicts_test_utils.consumer_unit_dict_1
        self.consumer_unit_test = create_objects_test_utils.create_test_consumer_unit(self.consumer_unit_test_dict, self.university)

        self.contract_test_dict = dicts_test_utils.contract_dict_1
        self.contract_test = create_objects_test_utils.create_test_contract(self.contract_test_dict, self.distributor, self.consumer_unit_test)

        self.energy_bill_test_dict = dicts_test_utils.energy_bill_dict_1

        self.test_date = date(2023, 1, 1)
        self.energy_bill_test_dict['date'] = self.test_date

    def test_check_energy_bill_still_do_no_exists(self):
        result = EnergyBill.check_month_and_year_already_exists(self.test_date, self.consumer_unit_test.id)

        assert not result

    def test_check_energy_bill_already_exists_for_month_and_year(self):
        create_objects_test_utils.create_test_energy_bill(self.energy_bill_test_dict, self.contract_test, self.consumer_unit_test)

        result = EnergyBill.check_month_and_year_already_exists(self.test_date, self.consumer_unit_test.id)

        assert result