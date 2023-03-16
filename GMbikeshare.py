import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities = ["Chicago", "New York City", "Washington"]
    while True:
        city = str(input('Would you like to see data for Chicago, New York City, or Washington? ')).title()
        if city in cities:
            break
        else:
            print ('That\'s not a valid city. Please enter \'Chicago\', \'New York City\', or \'Washington\'.')
            
    # get user input for month (all, january, february, ... , june or all)  
    
    months = ["January", "February", "March", "April", "May", "June", "All"]
    while True:
        month = str(input('Which month - January, February, March, April, May, June or All? ')).title ()
        if month in months:
            break
        else:
            print ('That\'s not a valid month. Please check your spelling.')
         
    # get user input for day of week (all, monday, tuesday, ... sunday or all)
    
    days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday", "All"]      
    while True:
        day = str(input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All? ')).title()
        if day in days:
            break
        else:
            print ('That\'s not a valid day. Please check your spelling. ')
            
    
    print('-'*40)
    return city, month, day


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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable  
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

       
    
    
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # find the most popular start station
    popular_start_station = df['Start Station'].mode()[0]
    # count for the most popular start station
    count_popular_start_station = df['Start Station'].value_counts()[popular_start_station]
    
    print('Most Popular Start Station:', popular_start_station)
    print('Count:', count_popular_start_station, '\n')

    # display most commonly used end station
    # find the most popular end station
    popular_end_station = df['End Station'].mode()[0]
     # count for the most popular end station
    count_popular_end_station = df['End Station'].value_counts()[popular_end_station]
    
    print('Most Popular End Station:', popular_end_station)
    print('Count:', count_popular_end_station, '\n')

    # display most frequent combination of start station and end station trip
    # create a new comlumn combining the start and end station names
    df['combination_station'] = df['Start Station']+" to "+df['End Station']
    # find the most populare combination station
    popular_combination_station = df['combination_station'].mode()[0]
    # count for the most popular combination station
    count_popular_combination_station = df['combination_station'].value_counts()[popular_combination_station]
    
    print('Most Popular Combination of Start and End Station:', popular_combination_station)
    print('Count:', count_popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # sum the Trip Duration column and convert the output from seconds to hours, minutes and seconds
    duration_mins,duration_secs = divmod(int(df['Trip Duration'].sum()),60)
    duration_hrs, duration_mins = divmod(duration_mins, 60)
    print('Total Travel Time:', duration_hrs, "hrs", duration_mins, "mins", duration_secs, "secs" )

    # display mean travel time
    # find the average Trip Duration and convert the output from seconds to hours, minutes and seconds
    mean_duration_mins,mean_duration_secs = divmod(int(df['Trip Duration'].mean()),60)
    mean_duration_hrs, mean_duration_mins = divmod(mean_duration_mins, 60)
    print('Mean Travel Time:', mean_duration_hrs, "hrs", mean_duration_mins, "mins", mean_duration_secs, "secs" )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Types:\n\n',user_types)

    # Display counts of gender
    # No Gender in Washington data-set, this if statement prevents error occurring if Washington selected on input
    if ('Gender' not in df):
        print ('\nGender information not available.\n')
    # Counts by Gender    
    else:
        gender = df['Gender'].value_counts()
        print('\nCount of Genders:\n',gender)

    # Display earliest, most recent, and most common year of birth
    # No Birth Year in Washington data-set, this if statement prevents error occurring if Washington selected on input
    if ('Birth Year' not in df):
        print ('Birth year information not available.')
    # Find most common Birth Year, earliest Birth Year and latest Birth Year
    else:
        popular_year = int(df['Birth Year'].mode()[0])
        print('\nMost Popular Birth Year:', popular_year)
        earliest_year = int(df['Birth Year'].min())
        print('Earliest Birth Year:', earliest_year)
        latest_year = int(df['Birth Year'].max())
        print('Most Recent Birth Year:', latest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_data(df):
    """
    Asks user to specify if they would like to see individual trip data.

    Returns 5 rows of the df dataframe each time 'Yes' is selected.
    Begins with row 0-4, and ascends each time 'Yes' is selected. 
    If 'No' is selected, no further data is returned.
    """
    start=0
     # get user input as to whether they would like to see trip data or not 
    selections = ["Yes", "No"]
    while True:
        selection=input('\n Would you like to see 5 lines of individual trip data? Type \'Yes\' or \'No\'').title()
        if selection in selections:
            break
        else:
            print ('That\'s not a valid response. Please enter \'Yes\', or \'No\'.')
    # for 'Yes' response the row index range is based on either the start row, or calculated based on the row index from the previous 'yes' or no 'response'.
    # the calculated rows of the df dataframe are printed
    while selection =='Yes':
        n=start+5
        print(df[start:n])
        # get user input as to whether they would like to see trip data or not 
        while True:
            selection=input('Would you like to see 5 more lines of data? Type \'Yes\' or \'No\'').title()
            if selection in selections:
                break
            else:
                print ('That\'s not a valid response. Please enter \'Yes\', or \'No\'.')
        start=n
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
