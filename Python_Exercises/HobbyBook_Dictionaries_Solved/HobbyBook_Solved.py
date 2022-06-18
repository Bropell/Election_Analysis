# @TODO: Your code here

first_dictionary = {
    "Pet_Name" : "Marley",
    "Pet_Age" : 2,
    "Pet_Hobbies" : ["Fetch", "Tug of War", "Hiking"],
    "wake_up_times" : {"weekday" : "7:30", "Saturday" : "9:00", "Sunday" : "10:00"}
}

print(f"My pet's name is {first_dictionary['Pet_Name']} and she is {first_dictionary['Pet_Age']} years old")
print(f"My pet has {len(first_dictionary['Pet_Hobbies'])} hobbies")
print(f"My pet's favorite hobby is {first_dictionary['Pet_Hobbies'][0]}")
print(f"On Sunday she likes to wake up at {first_dictionary['wake_up_times']['Sunday']} AM")
