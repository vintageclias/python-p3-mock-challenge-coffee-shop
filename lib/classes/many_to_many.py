class Coffee:
    all =[]
    # coffee is initialized with a name
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        # isinstance(val, str) needs to have str since name must be!!
        if isinstance(val, str) and 3 <= len(val) and not hasattr(self, 'name'):
            self._name = val

    def orders(self):
        # need to return list of Order objects with Coffee instances
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        # return unique list of customers who ordered this coffee
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        # need to return the # of orders for that coffee
        return len(self.orders())
    
    def average_price(self):
        # grab all orders for this coffee
        orders = self.orders()
        # returns 0 if coffee has never been ordered
        if len(orders) == 0:
            return 0
        # calculate total price of all orders
        total_price = sum([order.price for order in self.orders()])
        # return average price
        return total_price / self.num_orders()


class Customer:
    all = []
    # customer is initialized with a name
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val

    def orders(self):
        # return list of all orders for type of coffee
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        # return unique list of all coffees customer ordered / must be type Coffee
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        # set _price attribute
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.getter
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        # immutable error needs the hasattr
        if isinstance(val, float) and 1.0 <= val <= 10.0 and not hasattr(self, 'price'):
            self._price = val