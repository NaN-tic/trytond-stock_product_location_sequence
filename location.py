# This file is part of the stock_product_location_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
__all__ = ['ProductLocation']

__metaclass__ = PoolMeta


class ProductLocation:
    __name__ = 'stock.product.location'

    @staticmethod
    def default_sequence():
        return 1
