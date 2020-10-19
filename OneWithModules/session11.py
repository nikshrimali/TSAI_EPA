from functools import wraps, namedtuple
import random
from time import perf_counter
from collections import Counter
from datetime import date
from faker import Faker
fake = Faker()

# Check stats of the profiles for dicts and named tuples

def profile_stats(profiles, dict=False):
    '''
    Returns profile stats based on the random fake profiles generated
    largest blood type
    mean-current_location
    oldest_person_age
    average age

    :args profiles - Named tuple or a dictionary
    :args dict: bool operator which if flagged true will treat input as dictionary
    :returns largest_blood_grp, highest_age, average_age, mean_location
    '''
    
    blood_groups = []
    age_list = []
    location_list = []
    longitude = 0
    latitude = 0

    if dict:
        for index, profile in enumerate(profiles):
            blood_groups.append(profiles[index]['blood_group'])
            age_list.append((date.today() - profiles[index]['birthdate']).days)
            longitude += (profiles[index]['current_location'][0])
            latitude += (profiles[index]['current_location'][1])
            location_list.append([longitude, latitude])
            
    else:

        for index in (range(len(profiles[0]))):
            #Adding stats into the lists
            blood_groups.append(profiles[0][index].blood_group)
            age_list.append((date.today() - profiles[0][index].birthdate).days)
            longitude += (profiles[0][index].current_location[0])
            latitude += (profiles[0][index].current_location[1])
            location_list.append([longitude, latitude])
            
    blood_dict = Counter(blood_groups)
    largest_blood_grp =  max(blood_dict, key=blood_dict.get)
    highest_age = max(age_list)
    average_age = sum(age_list)/len(age_list)
    mean_location = sum(location_list[0])/len(location_list), sum(location_list[1])/len(location_list)
    # Printing the results

    print(f'The statistics of 10k profiles are  --Largest Bloodgroup - {largest_blood_grp}, -- Highest Age - {round(highest_age/365)}, -- Average Age - {round(average_age/365)}, -- mean location - {mean_location}')
    return largest_blood_grp, round(highest_age/365), round(average_age/365), mean_location

# Timer decorator - Performance evaluation
def timers(n_reps):
    '''Decorator with timers which takes no of iterations as arguments
    and returns avg time taken in each iteration
    :params n_reps : no of reps the functions needs to be tested'''
    def outer(fn):

        @wraps(fn)
        def inner(*args, **kwargs):
            times = []
            for _ in range(n_reps):
                start_time = perf_counter()
                fn(*args, **kwargs)
                end_time = perf_counter() - start_time
                times.append(end_time)

            print(f'Time taken to process {n_reps} is {sum(times)/n_reps}')
            return sum(times)/n_reps
        return inner
    return outer

# Dictionary of dictionary of profile data
def master_dict(fn):
    '''This decorator returns a dictionary of 10k profiles'''
    master_dict = dict()
        
    @wraps(fn)
    def store_profiles(n_params):
        profile_list = []
        for i in range(n_params):
            master_dict[i] = fake.profile() # Generate random fake profiles dicts into master dicts
            
        return master_dict # Return master dicts
    return store_profiles

@master_dict
def get_dict(n_params):
    '''Function with master_dict decorator, randomly generates profiles
    :args n_params: no of profiles required in the dictionary
    :returns none
    '''
    pass

@timers(1)
def log_dict_function():
    '''Function decorated with timers which takes no of iterations as arguments
    and returns avg time taken in each iteration'''
    a = get_dict(10000)
    profile_stats(a, dict=True)

# NamedTuple of NamedTuple of profile data

from functools import wraps, namedtuple

def master_profile(fn):
    '''This decorator returns a tuple of 10k profiles'''
    profile = namedtuple("profile", [*fake.profile().keys()])
    master_profile = namedtuple("master", "profiles")
        
    @wraps(fn)
    def store_profiles(n_params):
        profile_list = []
        for i in range(n_params):
            fake_profile = profile(**fake.profile()) # Generate random fake profiles
            profile_list.append(fake_profile) # Append it to a list
        return master_profile(tuple(profile_list)) # Put the entire list into a named tuple
    return store_profiles

@master_profile
def get_master_profilelist(n_params):
    pass

@timers(1)
def log_tuple_function():
    a = get_master_profilelist(10000)
    profile_stats(a)

# Stock market Scenario

def outer(fn):
    '''Creates a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close)'''

    def imaginary_stocks(n_indices):
        ''' Creates imaginary stock markets scenario'''
        master_market = namedtuple('master_market', 'all_indices')
        company_list = []

        img_stocks = namedtuple('img_stocks', 'name, symbol, start, open, high, end, close')
        for i in range(n_indices):
            # Registering fake companies
            fake_company = fake.company()
            random_indices = {
                "name":fake_company,
                "symbol":fake_company[0:2],
                "start":(random.randint(300,2500)),
                "open":None,
                "high":None,
                "end":None,
                "close":None
            }
            
            company = img_stocks(**random_indices)
            company_list.append(company)

        return master_market(company_list)
    return imaginary_stocks

@outer
def generate_tuples(index):
    pass

def move_market():
    '''Assigns a random weight to all the companies.'''
    rand_bool = bool(random.getrandbits(1))

    if rand_bool: # Market moves up
        return (0.95,1.2)
    else: # Market moves down
        return (0.8,1.12)

def daily_updates(market_tuple):

    ''' Calculate and show what value stock market started at, 
    what was the highest value during the day and where did it end. 

    :args market_tuple: Input named tuple containing list of all the market tuples
    :returns: Updated market tuple
    '''

    weights_list = []
    open_list = []
    a, b = move_market()

    # Assign the value if company is registered first time
    for index,_ in enumerate(market_tuple[0]):
        random_number = random.uniform(a, b)
        weights_list.append(random_number)
        company_tuple = market_tuple[0][index]
        new_updates = dict()

        if company_tuple.close:
            new_updates["open"] = round(company_tuple.close)
        else:
            new_updates["open"] = round(company_tuple.start)
        
        open_list.append(new_updates["open"])
        movement = round(new_updates["open"]*random_number)
        new_updates["close"] = movement
        new_updates["high"]  = round(max(new_updates["open"], movement))
        new_updates["end"]  = round(min(new_updates["open"], movement))

        market_tuple[0][index] = company_tuple._replace(**new_updates)
            
    market_tuple._replace(all_indices= market_tuple) # Updating master tuple with the updated values
    weights_list = [i/sum(weights_list) for i in weights_list] # Normalizing the values
    market_performance = [round(i*j) for i,j in zip(weights_list, open_list)] # Multiplying the values with the opening values

    return market_tuple, sum(market_performance)