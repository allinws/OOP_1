car_models = [
    {'model': 'Model X', 'weight': 1100}, 
    {'model': 'Model S', 'weight': 1300}, 
    {'model': 'Model Y', 'weight': 1700}, 
    {'model': 'Model 3', 'weight': 1900},
]

car_prices_list = {'Model S': 1555000, 'Model X': 1588000, 'Model 3': 629000, 'Model Y': 689000}


class CarPriceClass():

    def __init__(self, car_prices_list):
        self.car_prices_list = car_prices_list

    def return_car_price(self, model_name):
        return self.car_prices_list[model_name]


class CarPrinterClass(CarPriceClass):

    def __init__(self, car_prices_list, car_models):
        CarPriceClass.__init__(self, car_prices_list)
        # super().__init__(car_prices_list) # Går lika bra
        self.car_models = car_models
    
    def print_car_prices(self):
        car_model_tuples = []
        dicts_missing_key = []
        for model in self.car_models:
            model_name = model.get('model')
            dicts_missing_key.append(model)
            price = self.return_car_price(model_name)
            car_tuple = (model_name, price)
            car_model_tuples.append(car_tuple)
        print(car_model_tuples)


car_instance = CarPrinterClass(car_models=car_models, car_prices_list=car_prices_list)

car_instance.print_car_prices()