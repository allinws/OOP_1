import datetime
import pytz

class BaseTimeHandler():

    def __init__(self, timezone_str):
        self.timezone_str = timezone_str
        self.timezone_obj = None
        self.update_timezone_object()

    def update_timezone_object(self):
        try:
            self.timezone_obj = pytz.timezone(self.timezone_str)
        except:
            raise Exception('Timezone couldnt be found!')

    def print_current_time(self):
        current_time = datetime.datetime.now(self.timezone_obj)
        print(f'Current time in {self.timezone_str} is {current_time}') 

    def print_time_tomorrow(self):
        time_tomorrow = datetime.datetime.now(self.timezone_obj) + datetime.timedelta(days=1)
        print(f'Time in 24 hours in {self.timezone_str} is {time_tomorrow}') 


class StockholmTimeHandler(BaseTimeHandler):
    pass

class LondonTimeHandler(BaseTimeHandler):
    pass


sthlm_instance = StockholmTimeHandler(timezone_str='Europe/Stockholm')
sthlm_instance.print_current_time()
sthlm_instance.print_time_tomorrow()

london_instance = LondonTimeHandler(timezone_str='Europe/London')
london_instance.print_current_time()
london_instance.print_time_tomorrow()