print('       METRO NAVIGATOR            ')
from tabulate import tabulate
import pandas as pd

# List of metro stations
stations = [
    [1, 'RAIDURG'], [2, 'HITEC CITY'], [3, 'DURGAM CHERUVU'], [4, 'MADHAPUR'],
    [5, 'PEDDAMMA GUDI'], [6, 'JUBILEE HILLS CHECKPOST'], [7, 'ROAD NO.5 JUBILEE HILLS'],
    [8, 'YUSUFGUDA'], [9, 'MADHURA NAGAR'], [10, 'AMEERPET'], [11, 'BEGUMPET'],
    [12, 'PRAKASH NAGAR'], [13, 'RASOOLPURA'], [14, 'PARADISE'], [15, 'PARADE GROUND'],
    [16, 'SECUNDERABAD EAST'], [17, 'METTUGUDA'], [18, 'TARNAKA'], [19, 'HABSIGUDA'],
    [20, 'NGRI'], [21, 'STADIUM'], [22, 'UPPAL'], [23, 'NAAGOL']
]

# Display metro station data in table format
print(tabulate(stations, headers=["Station No.", 'Station Name']))

# Travel data (distance, time, and fare for each segment between stations)
distances = [1.5, 0.8, 6.9, 16.9, 0.9, 0.6, 13.4, 1.4, 0.7, 1.6, 1.4, 1.1, 1, 1.2, 1.6, 1.9, 1.3, 1.6, 0.9, 1.2, 1.1, 1]
times = [3, 1, 2, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 2, 2]
fares = [15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# Prompt user for station input
try:
    starting_station = int(input('Enter your current station number: '))
    destination_station = int(input('Enter your destination station number: '))

    # Check if station numbers are valid
    if starting_station < 1 or starting_station > len(stations) or destination_station < 1 or destination_station > len(stations):
        print('Invalid station number. Please choose a valid station.')
    else:
        # Initialize journey details
        total_distance, total_time, total_fare = 0, 0, 0

        # Calculate total distance, time, and fare based on user input
        if starting_station < destination_station:
            for i in range(starting_station - 1, destination_station - 1):
                total_distance += distances[i]
                total_time += times[i]
                total_fare += fares[i]
        elif starting_station > destination_station:
            for i in range(starting_station - 2, destination_station - 2, -1):  # Reverse traversal for backward journey
                total_distance += distances[i]
                total_time += times[i]
                total_fare += fares[i]

        # Create a summary of the journey
        journey_summary = {'Distance (km)': [total_distance], 'Time (min)': [total_time], 'Cost (₹)': [total_fare]}
        journey_df = pd.DataFrame(journey_summary)
        
        print("\nJourney Summary:")
        print(journey_df.to_string(index=False))

except ValueError:
    print("Please enter a valid numeric station number.")
