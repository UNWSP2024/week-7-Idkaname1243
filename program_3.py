# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]

    data = []
    while True:
        try:
            year = int(input("Enter the year (or type '0' to stop): "))
            if year == 0:
                break
            state = input("Enter the name of the state: ")
            population = int(input(f"Enter the population of {state}: "))
            data.append([year, state, population])
        except ValueError:
            print("Invalid input. Please enter valid information.")
    try:
        query_year = int(input("Enter the year for which you want to calculate the total population: "))
        total_population = sum([entry[2] for entry in data if entry[0] == query_year])
        if total_population:
            print(f"The total population for the year {query_year} is {total_population}.")
        else:
            print(f"No data available for the year {query_year}.")
    except ValueError:
        print("Invalid input for the year.")

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year


def sum_population_for_year(all_entered_values, year_to_sum):
    print()

# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they enterd 2011 for the year to sum.

# print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
