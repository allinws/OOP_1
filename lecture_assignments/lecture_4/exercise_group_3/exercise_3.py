
all_orders = [{'order_number': 1, 'fullfilled': False}, {'order_number': 2, 'fullfilled': True}, {'order_number': 3, 'fullfilled': True},  {'order_number': None, 'fullfilled': True}]

class OrderHandler():

    def __init__(self, orders):
        self.orders = orders
        self.invalid_orders_count = 0
        self.fullfilled_order_count = 0


    def validate_orders(self):
        for order in self.orders:
            order_number = order.get('order_number', None)
            if order_number is None:
                raise Exception
    
    def is_order_fullfilled(self, order):
        return order.get('fullfilled')

    def update_order_counts(self):
        try:
            self.validate_orders()
        except:
            self.invalid_orders_count += 1
        for order in self.orders:
            if self.is_order_fullfilled(order):
                self.fullfilled_order_count += 1

    def print_order_counts(self):
        print(f'Invalid orders count', self.invalid_orders_count)
        print(f'Fulfilled orders count', self.fullfilled_order_count)


instance = OrderHandler(all_orders)
instance.update_order_counts()
instance.print_order_counts()

