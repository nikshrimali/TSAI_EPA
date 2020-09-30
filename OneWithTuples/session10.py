from functools import wraps, namedtuple
from time import perf_counter
from collections import Counter
from datetime import date
from faker import Faker
fake = Faker()

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
def log_function():
    '''Function decorated with timers which takes no of iterations as arguments
    and returns avg time taken in each iteration'''
    a = get_dict(10000)
    profile_stats(a, dict=True)


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
        return master_profile(profile_list) # Put the entire list into a named tuple
    return store_profiles

@master_profile
def get_master_profilelist(n_params):
    pass

@timers(1)
def log_tuplefunction():
    a = get_master_profilelist(10000)
    profile_stats(a)