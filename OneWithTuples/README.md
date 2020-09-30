# Named Tuples

## <b> Functions Implemented </b>

##  profile_stats(profiles, dict=False):
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

## timers(n_reps):
    '''Decorator with timers which takes no of iterations as arguments
    and returns avg time taken in each iteration
    :params n_reps : no of reps the functions needs to be tested'''

## master_dict(fn):
    '''This decorator returns a dictionary of 10k profiles'''

## log_dict_function():
    '''Function decorated with timers which takes no of iterations as arguments
    and returns avg time taken in each iteration'''

## master_profile(fn):
    '''This decorator returns a tuple of 10k profiles'''

## outer(fn):
    '''A decorator that creates a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close)'''

## move_market():
    '''Assigns a random weight to all the companies.'''

## daily_updates(market_tuple):

    ''' Calculate and show what value stock market started at, 
    what was the highest value during the day and where did it end. 

    :args market_tuple: Input named tuple containing list of all the market tuples
    :returns: Updated market tuple
    '''


## <b>Testcases Implemented</b>

##  test_readme_exists():
    Checks if README.md exists

##  test_readme_contents():
    Contents of readme file has been properly written or not
   

##  test_readme_file_for_formatting():
    Checks for Readme File formatting

##  test_function_name_had_cap_letter():
    Raises error if Functions has capital letter

## test_perf_tuples_dicts():
    '''Checks if namedtuples(named_tuples) performs better than dict(dict) '''
