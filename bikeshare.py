import pandas as pd
import time

# TO DO: set option "display.expand_frame_repr" à false for expand the output display
pd.set_option('display.expand_frame_repr', False)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
        
    print('Hello! Let\'s explore some US bikeshare data!')
    city  = ""
    month = ""
    day   = ""
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city == "":
          if city == "": 
             city = input("enter city name :")
             city = validateCity(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    while month == "":
          if month == "":
             month = input("enter name of the month or \"all\" to apply no month :")
             month = validateMonth(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day == "":
          if day == "":
             day = input("enter name of the day of week or \"all\" to apply no day :")
             day = validateDay(day)

    print('-'*40)
        
    return city, month, day


"""
   Test the value of city 

"""
def validateCity(city):
        
    value = ""
    for key in CITY_DATA:
        if key == city:
           value = city
           break
        
    if value == "":
       print('invalid inputs name of city')
       
    return value

"""
   Test the value of month 

"""
def validateMonth(month):
        
    value = ""
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    for key in months:
        if key == month:
           value = month
           break
        
    if value == "":
       print('invalid inputs name of month')
       
    return value


"""
   Test the value of day 

"""
def validateDay(day):
        
    value = ""
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    for key in days:
        if key == day:
           value = day
           break
        
    if value == "":
       print('invalid inputs name of day')
       
    return value

"""
   display function

"""
def display(df):
    row_number = 5
    msg = "do you want to see 5 lines of raw data ? :"
    while True:
          answer = input(msg)
          if answer == "yes":
             print(df.head(row_number))
             row_number+=5
             msg = "do you want to see 5 more lines of raw data ? :"
          if answer == "no":
             break
          print('-'*40) 

"""
   time stats function

"""
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    # TO DO: display data raw (yes/no)
    display(df)

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)    

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular day of week:', popular_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


"""
   station stats function

"""
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    # TO DO: display data raw (yes/no)
    display(df)

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts()
    popular_used_start_station = start_station.mode()[0]
    print('Most commonly used start station:', df['Start Station'].get(popular_used_start_station))
    
    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts()
    popular_used_end_station = end_station.mode()[0]
    print('Most commonly used end station:', df['End Station'].get(popular_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df_combination = df['Start Station'] + df['End Station']
    most_frequent_combination_start_station_end_station = df_combination.mode()[0]
    print('Most frequent combination of start station and end station trip:', most_frequent_combination_start_station_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

"""
   trip duration stats function

"""
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    # TO DO: display data raw (yes/no)
    display(df)

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    # TO DO: display the minimum travel time
    min_travel_time = df['Trip Duration'].min()
    print('Minimum travel time:', min_travel_time)

    # TO DO: display the maximum travel time
    max_travel_time = df['Trip Duration'].max()
    print('Maximum travel time:', max_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


"""
   test of column name exist function

"""
def is_column_exists(column_list,name):
    for col_name in column_list:
        if name == col_name:
            return True

    return False



"""
   user stats function

"""
def user_stats(df):
    """Displays statistics on bikeshare users."""

    # TO DO: display data raw (yes/no)
    display(df)

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].count()
    print('Counts of user types:', counts_user_types)

    # TO DO: Display counts of gender
    if is_column_exists(df.columns,"Gender"):
       counts_gender = df['Gender'].count()
       print('counts of gender:', counts_gender)

    if is_column_exists(df.columns,"Birth Year"):
       # TO DO: Display earliest year of birth
       earliest_year_of_birth = df['Birth Year'].min()
       print('earliest year of birth:', earliest_year_of_birth)

       # TO DO: most recent year of birth
       most_recent_year_of_birth = df['Birth Year'].max()
       print('most recent year of birth:', most_recent_year_of_birth)

       # TO DO: most common year of birth
       most_common_year_of_birth = df['Birth Year'].mode()[0]
       print('most common year of birth:', most_common_year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


"""
   load data function

"""
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    

    return df

"""
   Main

"""

def main():
    while True:
        city, month, day = get_filters()
        print(city + ' - ' + month + ' - ' + day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

if __name__ == "__main__":
        main()
