import requests
import json

#step 1: read all state codes from a file
def get_state_codes():
    #open file that has state/ territory code
    with open("/home/ubuntu/hw5/states_territories.txt", "r") as file:
        #read each line, remove extra spaces, and make it lowercase
        codes = [line.strip().lower() for line in file if line.strip()]
    return codes


#step 2: get covid data from api and save to a json file for each state
def fetch_and_save_state_data(state_code):
    #build url with state code
    url = f"https://api.covidtracking.com/v1/states/{state_code}/daily.json"
    #ask website for data
    response = requests.get(url)
    
    #if it worked, status 200, then save data
    if response.status_code == 200:
        data = response.json()
        filename = f"{state_code}.json"
        #save data to a json file
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Saved data for {state_code} to {filename}")

#step 3: analyze a state's covid data from the saved json file
if __name__ == "__main__":
    state_codes = get_state_codes()
            
    for code in state_codes:
        fetch_and_save_state_data(code)

from collections import defaultdict
from statistics import mean

def analyze_state_data(state_code):
    filename = f"{state_code}.json"
    try:
        #open file and load data
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return

    if not data:
        print(f"No data for {state_code}")
        return

#lists and dictionaries to store dif kinds of info
    daily_cases = []
    no_case_dates = []
    month_totals = defaultdict(int)

#go through each day's data
    for entry in data:
        date = str(entry.get("date", ""))
        increase = entry.get("positiveIncrease", 0)

        if not date:
            continue #skip

#save daily number of new cases
        daily_cases.append((date, increase))

#track dates where there were 0 new cases
        if increase == 0:
            no_case_dates.append(date)

#get first 6 characters of date
        month = date[:6]
        month_totals[month] += increase #add to months total

#sort by most cases in a single day
    sorted_cases = sorted(daily_cases, key=lambda x: x[1], reverse=True)
    #calc average daily new cases
    avg_daily = mean([c[1] for c in daily_cases])
    #get day w highest number of noew cases
    highest_date = sorted_cases[0][0]
    highest_value = sorted_cases[0][1]
    #get most recent day w 0 new cases
    most_recent_zero = max(no_case_dates) if no_case_dates else "N/A"

    #sort months by total cases
    sorted_months = sorted(month_totals.items(), key=lambda x: x[1], reverse=True)
    highest_month = sorted_months[0][0]
    lowest_month = sorted_months[-1][0]

    #show results
    print("\nCovid confirmed cases statistics")
    print(f"State name: {state_code.upper()}")
    print(f"Average number of new daily confirmed cases: {avg_daily:.2f}")
    print(f"Date with the highest new number of covid cases: {highest_date} ({highest_value})")
    print(f"Most recent date with no new covid cases: {most_recent_zero}")
    print(f"Month and Year with the highest new number of covid cases: {format_month(highest_month)}")
    print(f"Month and Year with the lowest new number of covid cases: {format_month(lowest_month)}")

#change date format
def format_month(month_str):
    year = month_str[:4]
    month = month_str[4:]
    return f"{month}/{year}"

##3

def main():
    state_codes = get_state_codes()  # use the helper function you already wrote
    #for each state, get and analyze data
    for code in state_codes:
        fetch_and_save_state_data(code)
        analyze_state_data(code)

#run program!
if __name__ == "__main__":
    main()
