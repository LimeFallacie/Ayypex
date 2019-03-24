# Ayypex

![Alt Text](https://github.com/LimeFallacie/Ayypex/blob/master/static/demo.gif)

Ayypex Carpark sniffer

This program aims to take in a user address (most likely postal code);
and returns the nearest available carparks with open lots.

Program flow:

1) User Input (postal code) is converted to SVY21 format (OneMap REST API)

2) Use User_SVY21_location to locate nearest carparks (HDB Carpark Information)

3) Check for available lots in listed nearby carparks (data.gov carpark availability)

4) Generate route maps (currently PNG) for each of the shortlisted nearby carparks with available lots

APIs used:

- OneMap
- HDB Carpark Information 
- Carpark Availability
