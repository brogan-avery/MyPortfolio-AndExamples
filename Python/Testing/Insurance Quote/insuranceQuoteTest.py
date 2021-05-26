'''
Author: Brogan Avery
Date: 2020/08/30
Project Title: Auto Insurance Quote test
Desc: unit test
'''

import unittest
import insuranceQuote as iq
from insuranceQuote import *

class MyTestCase(unittest.TestCase):
    def test_get_base_rate(self):
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 16, 'Coverage Type': 'State Minimum', 'Coverage Rate': '2593.00'}, get_base_rate("Jane", "Smith",16,"S"))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 25, 'Coverage Type': 'Liability Coverage', 'Coverage Rate': '691.00'}, get_base_rate("Jane", "Smith",25,"L"))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 36, 'Coverage Type': 'Full Coverage', 'Coverage Rate': '1564.00'}, get_base_rate("Jane", "Smith",36,"F"))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 54, 'Coverage Type': 'State Minimum', 'Coverage Rate': '525.00'}, get_base_rate("Jane", "Smith",54,"s"))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 59, 'Coverage Type': 'Liability Coverage', 'Coverage Rate': '560.00'}, get_base_rate("Jane", "Smith",59,"l"))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 80, 'Coverage Type': 'Full Coverage', 'Coverage Rate': '1402.00'}, get_base_rate("Jane", "Smith",80,"f"))

    def test_add_accident_fee(self):
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 16, 'Coverage Type': 'State Minimum', 'Coverage Rate': '3656.13'}, add_accident_fee({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 16, 'Coverage Type': 'State Minimum', 'Coverage Rate': '2593.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 25, 'Coverage Type': 'Liability Coverage','Coverage Rate': '974.31'}, add_accident_fee({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 25, 'Coverage Type': 'Liability Coverage', 'Coverage Rate': '691.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 36, 'Coverage Type': 'Full Coverage', 'Coverage Rate': '2205.24'}, add_accident_fee({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 36, 'Coverage Type': 'Full Coverage', 'Coverage Rate': '1564.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 54, 'Coverage Type': 'State Minimum', 'Coverage Rate': '740.25'}, add_accident_fee({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 54, 'Coverage Type': 'State Minimum', 'Coverage Rate': '525.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 59, 'Coverage Type': 'Liability Coverage','Coverage Rate': '789.60'}, add_accident_fee({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 59, 'Coverage Type': 'Liability Coverage', 'Coverage Rate': '560.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 80, 'Coverage Type': 'Full Coverage','Coverage Rate': '1976.82'}, add_accident_fee({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 80, 'Coverage Type': 'Full Coverage', 'Coverage Rate': '1402.00'}))

    def test_add_discount(self):
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 16, 'Coverage Type': 'State Minimum','Coverage Rate': '2333.70'}, add_discount({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 16, 'Coverage Type': 'State Minimum','Coverage Rate': '2593.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 25, 'Coverage Type': 'Liability Coverage','Coverage Rate': '621.90'}, add_discount({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 25, 'Coverage Type': 'Liability Coverage','Coverage Rate': '691.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 36, 'Coverage Type': 'Full Coverage','Coverage Rate': '1407.60'}, add_discount({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 36, 'Coverage Type': 'Full Coverage','Coverage Rate': '1564.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 54, 'Coverage Type': 'State Minimum','Coverage Rate': '472.50'}, add_discount({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 54, 'Coverage Type': 'State Minimum', 'Coverage Rate': '525.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 59, 'Coverage Type': 'Liability Coverage','Coverage Rate': '504.00'}, add_discount({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 59, 'Coverage Type': 'Liability Coverage','Coverage Rate': '560.00'}))
        self.assertEqual({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 80, 'Coverage Type': 'Full Coverage','Coverage Rate': '1261.80'}, add_discount({'First Name': 'Jane', 'Last Name': 'Smith', 'Age': 80, 'Coverage Type': 'Full Coverage','Coverage Rate': '1402.00'}))


if __name__ == '__main__':
    unittest.main()
