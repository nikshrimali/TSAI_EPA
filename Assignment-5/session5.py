import time
import math

def time_it(fn, *args, repetitons= 1, **kwargs):
    '''Calculates the average time taken to perform any transaction by \
        Function fn averaging the total time taken for transaction over Repetations'''
    total_time = []

    for _ in range(repetitons):
        start_time = time.perf_counter()
        ins_time = fn(*args,**kwargs)
        end_time = time.perf_counter()
        ins_time = end_time - start_time
        total_time.append(ins_time)

    return(avg_time(total_time))


def avg_time(my_list):
    print('sum :', sum(my_list))
    print('len :',len(my_list))
    return sum(my_list)/len(my_list)


def squared_power_list(number, start, end):
    '''Returns a list of numbers created by adding powers of 2 \
        from start till end to number n

        >>squared_power_list(2,0,5) = [1, 2, 4, 8, 16, 32]'''

    powered_list=[]

    if start >= 0 and end > 0 and end > start:
        for j in range(end+1-start):
            powered_list.append(number**j)
    else:
        raise ValueError('Start and end values must be positive numbers and end > start')

    return powered_list

# Polygon Area

def polygon_area(side_length, sides):
    '''Calcuates the area of a regular polygon for\
        no of sides of side_length'''

    if sides < 6:
        perimeter = side_length*sides
        apothem = side_length/(2*(math.tan(math.pi/sides)))
        area = perimeter*apothem/2
    else:
        raise ValueError('Calculation can be done only for 6 sides polygon')
    return round(area,2)

# Temperature Converter

def temp_converter(base_temp, temp_given_in):
    '''Convert the temperature base_temp from Farhenite \
        to Celcius or Celcius to Farhenite as mentioned in temp_given_in

        >> temp_converter(100,'c') = 37.76'''
    new_temp = None

    if temp_given_in == 'f':
        new_temp = (base_temp - 32)/1.8

    elif temp_given_in == 'c':
        new_temp = (base_temp*1.8) + 32

    else:
        raise ValueError('Only farhenite -f and celcius -c are allowed')

    return round(new_temp,2)

# Speed Converter

def speed_converter(speed, dist, time):
    '''The input speed is assumed in kmph, conversion can be made for \
        any combination of conversion metrics of distance and time as mentioned below'''

    DIST_METRIC = {
        'm': 1000,
        'km': 1,
        'yrd': 1093.613,
        'ft': 3280.84,
    }

    TIME_METRIC = {
        'ms': 3600000,
        's': 3600,
        'm': 60,
        'hr': 1,
        'day': 1/24,
        }

    converted_speed = None

    if dist in DIST_METRIC and time in TIME_METRIC:
        converted_speed = speed * (DIST_METRIC[dist]/TIME_METRIC[time])

    else:
        raise ValueError('Incorrect metric used for distance and time')

    return round(converted_speed,2)
