
import datetime

swe_month_translation = {1: 'Januari', 2: 'Februari', 3: 'Mars'}

def return_datetime_object(datetime_str):
    try:
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    except Exception as e:
        raise Exception(f'Should give format as format 2022-02-02 {e}')

#dt_obj = return_datetime_object('2022-02-01')


def return_swedish_month_name(month):
    try:
       return swe_month_translation[month]
    except KeyError:
        raise KeyError('Didnt found month')

# month = return_swedish_month_name(3)
# print(month)


try:
    my_date = return_datetime_object('2022-03-02')
    my_month = return_swedish_month_name(my_date.month)
except KeyError:
    print('KeyError Exception happened')
except Exception as e:
    print(e)
    print('General exception happened')


try:
    my_date = return_datetime_object('2022-10-01')
    my_month = return_swedish_month_name(my_date.month)
except KeyError:
    print('KeyError Exception happened')
except Exception as e:
    print(e)
    print('General exception happened')
