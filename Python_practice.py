counties = ["Arapahoe", "Denver", "Jefferson", ]
if "El Paso" in counties:
        print("El Paso is in the list of counties.")
else:
        print("El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
        print("Only Arapahoe is in the list of counties.")
else:
        print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
        print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
        print(county)

for voters in counties_dict.values():
        print(voters)

for county in counties_dict:
        print(counties_dict[county])

for county in counties_dict:
        print(counties_dict.get(county))

for key, value in counties_dict.items():
        print(key, value)

for key, value in counties_dict.items():
        print(key, "county has", value, "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
        print(county_dict)

for county_dict in voting_data:
        for value in county_dict.values():
                print(value)

for county_dict in voting_data:
     print(county_dict['registered_voters'])

for county_dict in voting_data:
        print(county_dict['county'])

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
        print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

