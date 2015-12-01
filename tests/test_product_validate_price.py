# This file is part of the product_validate_price module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductValidatePriceTestCase(ModuleTestCase):
    'Test Product Validate Price module'
    module = 'product_validate_price'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductValidatePriceTestCase))
    return suite