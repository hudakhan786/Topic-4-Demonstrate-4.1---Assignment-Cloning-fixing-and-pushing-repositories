import json

# Load the data from the JSON file
with open('school_data.json') as f:
    data = json.load(f)

# Function to print universities with a graduation rate for women over 50%
def graduation_rate_for_women(data):
    print("Universities with a graduation rate for women over 50%:")
    for record in data:
        try:
            graduation_rate_women = record.get('Graduation rate  women (DRVGR2020)')
            if graduation_rate_women is not None and graduation_rate_women > 50:
                print(f"University: {record['instnm']}")
                print(f"Graduation Rate for Women: {graduation_rate_women}%")
                print()
        except KeyError:
            continue

# Function to print universities with a total price for in-state students living off campus over $50,000
def total_price_instate_offcampus(data):
    print("Universities with a total price for in-state students living off campus over $50,000:")
    for record in data:
        try:
            total_price = record.get('Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)')
            if total_price is not None and total_price > 50000:
                print(f"University: {record['instnm']}")
                print(f"Total price for in-state students living off campus: ${total_price:,.2f}")
                print()
        except KeyError:
            continue

# Run the functions
graduation_rate_for_women(data)
total_price_instate_offcampus(data)
