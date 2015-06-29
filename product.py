# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction

__all__ = ['Template']
__metaclass__ = PoolMeta


class Template:
    __name__ = 'product.template'

    @classmethod
    def __setup__(cls):
        super(Template, cls).__setup__()
        cls._error_messages.update({
                'list_price_error': 'You can not set "%(product)s" '
                    'the list price (%(list_price)s) lesser '
                    'than the cost price (%(cost_price)s).',
                })

    @classmethod
    def validate(cls, records):
        super(Template, cls).validate(records)
        if Transaction().context.get('validate_price', True):
            cls.validate_price(records)

    @classmethod
    def validate_price(cls, records):
        for record in records:
            if record.list_price < record.cost_price:
                cls.raise_user_error('list_price_error', {
                        'product': record.rec_name,
                        'list_price': record.list_price,
                        'cost_price': record.cost_price,
                        })
