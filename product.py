# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta


__all__ = ['Template']
__metaclass__ = PoolMeta


class Template:
    __name__ = 'product.template'

    @classmethod
    def __setup__(cls):
        super(Template, cls).__setup__()
        cls._error_messages.update({
                'list_price_error': 'You can not set the list price lesser '
                    'than the cost price.',
                })

    @classmethod
    def validate(cls, records):
        super(Template, cls).validate(records)
        cls.validate_price(records)

    @classmethod
    def validate_price(cls, records):
        for record in records:
            if record.list_price < record.cost_price:
                cls.raise_user_error('list_price_error')
