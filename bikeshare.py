import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = [ 'all','saturday','sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_entered =  input("Enter the name of the city you want to analyze.. chicago, new york city, washington..?\n")
        if city_entered.lower() in CITY_DATA:
            city = city_entered.lower()
            break
        else:
            print("Enter a valid value  chicago, new york city, washington ")   
            continue 


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_entered = input("Enter the month you want to filter data to  all, january, february, ... , june\n")
        if month_entered.lower() in months:
            month = month_entered.lower()
            break
        else:
            print("Enter valid month value  all, january, february, ... , june")
            continue    



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_entered = input("What is the name of day you want to filter for all, monday, tuesday, ... sunday\n")
        if day_entered.lower() in days:
            day = day_entered.lower()
            break
        else:
            print("Enter a vaild day value all, monday, tuesday, ... sunday ")    
            continue
          

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df["month"].mode()[0]
    print("The most common month is {}".format(months[month-1]))


    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print("The most common day is {} ".format(day))


    # TO DO: display the most common start hour

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract hour from the Start Time column to create an hour column
    df["hour"] = df["Start Time"].dt.hour

    # find the most popular hour
    popular_hour = df["hour"].mode()[0]

    print('Most Popular Start Hour:', popular_hour)
    
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commom start station is {}".format(most_common_start_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}".format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip

    combined_trip = df['Start Station'] + df['End Station']
    print("The most frequent combination trip is {}".format(combined_trip.mode()[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
          
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time  is {} ".format(total_travel_time))


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("Average travel time is {}".format(average_travel_time))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df["User Type"].value_counts()
    print(user_count)

    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in (df.columns):
        year = df['Birth Year']
        print("The common year in {} and the most recent year is {} and the most earliest year is {}".format(year.mode()[0],year.max(),year.min()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Display Raw data  """
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    if view_data.lower() == "yes":
        start_loc = 0
        while (view_data != 'no'):
           print(df.iloc[0:start_loc + 5])
           start_loc += 5
           view_display = input("Do you wish to continue?: ").lower()
           if view_display != 'no':
              continue
           else:
              break
           
    
    


    

    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
