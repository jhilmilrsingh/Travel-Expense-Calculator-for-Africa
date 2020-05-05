country  = ["Nigeria: 1550", "Ethiopia: 1500", "Egypt: 1450", "DR Congo: 1400", \
          "Tanzania: 1350", "South Africa: 1325", "Kenya: 1320", "Uganda: 1320", \
          "Algeria: 1320", "Sudan: 1310", "Morocco: 1310", "Angola: 1305", \
          "Mozambique: 1300", "Ghana: 1290", "Madagascar: 1240", "Cote d'lvoire: 1220," \
          "Cameroon: $1210", "Niger: $1200", "Burkina Faso: $1150", "Malawi: $1145", \
          "Mali: 1140", "Zambia: 1130", "Zimbabwe: 1122", "Senegal: 1120", "Chad: 1100" \
          "Somalia: 1100", "Guinea: 1099", "South Sudan: 1080", "Rwanda: 1070", "Benin: 1070" \
          "Tunisia: 1065", "Burundi: 1065", "Togo: 1050", "Sierra Leone: 1025", "Libya: 1020" \
          "Congo: 1000", "Eritea: 950", "Liberia: 930", "Central Africam Republic: 930", \
          "Mauritania: 910", "Namibia: 900", "Botswana: 850", "Gambia: 845", \
          "Gabon: 840", "Guinea-Bissau: 800", "Swaziland: 800", "Equatorial Guinea: 795", \
          "Mauritius: 790", "Djibouti: 790", "Comoros: 790", "Cabo Verde: 750", \
          "Sao Tome & Principe: 750", "Seychelles: 700"]

country_chosen = input("Which country are you visiting in Africa: ")

for element in country:
    x = element.split(':')
    listeditem = x[0]
    y = x[1]

    if country_chosen == listeditem:
        print("The airfare for", country_chosen, "is $" + str(y))

hotel_booking_cost  = ["Nigeria: 220", "Ethiopia: 150", "Egypt: 112", "DR Congo: 120", \
          "Tanzania: 210", "South Africa: 145", "Kenya: 170", "Uganda: 168", \
          "Algeria: 186", "Sudan: 199", "Morocco: 122", "Angola: 175", \
          "Mozambique: 200", "Ghana: 119", "Madagascar: 152", "Cote d'lvoire: 223," \
          "Cameroon: 115", "Niger: 186", "Burkina Faso: 193", "Malawi: 147", \
          "Mali: 123", "Zambia: 146", "Zimbabwe: 170", "Senegal: 148", "Chad: 199" \
          "Somalia: 211", "Guinea: 202", "South Sudan: 118", "Rwanda: 115", "Benin: 127" \
          "Tunisia: 134", "Burundi: 167", "Togo: 189", "Sierra Leone: 222", "Libya: 176" \
          "Congo: 105", "Eritea: 100", "Liberia: 102", "Central Africam Republic: 110", \
          "Mauritania: 112", "Namibia: 101", "Botswana: 95", "Lesotho: 98", "Gambia: 93", \
          "Gabon: 90", "Guinea-Bissau: 90", "Swaziland: 92", "Equatorial Guinea: 80", \
          "Mauritius: 85", "Djibouti: 87", "Comoros: 80", "Cabo Verde: 75", \
          "Sao Tome & Principe: 70", "Seychelles: 63"]

country_chosen_again = input("To find out what is the hotel cost per night, confirm which country in Africa are you visiting: ")

for element in hotel_booking_cost:
    x = element.split(':')
    listeditem = x[0]
    y = x[1]    

    if country_chosen_again == listeditem:
        print("The hotel booking cost per night for", country_chosen_again, "is $" + str(y))
        num_of_nights = input("How many nights are you staying: ")
        y1 = int(y)
        
rental_car = input("Will you be renting a car, Yes/No ")

if rental_car == "Yes":

    days = int(input("How many days are you renting the car for: "))
    rentalcartype = input("With the choices of SUV, MPV, Sedan and Luxury, which car type would you like to rent:")

    if rentalcartype == "SUV":
        cost = 65 * days
        print ("The cost for renting a SUV is $65/day.")

    if rentalcartype == "MPV":
        cost = 75 * days
        print ("The cost for renting a MPV is $75/day.")

    if rentalcartype == "Sedan":
        cost = 50 * days
        print ("The cost for renting a Sedan is $50/day.")

    if rentalcartype == "Luxury":
        cost = 200 * days
        print ("The cost for renting a Luxury is $200/day.")

else:
    pass

print(" ")
print ("You are visiting", country_chosen, "in Africa.")

if country_chosen == "Kenya" or "Tanzania" or "South Africa" or \
   "Egypt" or "Comoros" or "Djibouti" or "Malawi" or "Rwanda" or "Togo" \
   or "Zambia" or "Zimbabwe":
    print("You will need a visa on arrival for", country_chosen)

else:
    pass

for element in country:
    x = element.split(':')
    listeditem = x[0]
    y = x[1]
    
    if country_chosen == listeditem:
        
        print("The airfare will cost $" + str(y))
        flightExpense = int(y)
        totalNumNights = int(num_of_nights)
        hotelExpense = y1 * totalNumNights
        print ("The hotel expense will cost $" + str(hotelExpense))
        
if rental_car == "Yes":
    
    price = cost
    print ("The rental car expense of a", rentalcartype, "for", days, "days will cost $" + str(cost))
    print ("The total travelå expense will cost $" + str(flightExpense + hotelExpense + price))   

else:
    pass

    print ("The total travel expense will cost $" + str(flightExpense + hotelExpense))   
    
print ("Have a blessed trip visiting", country_chosen, "in Africa!") 
