# This pulls up a GUI that prompts an input of a major US city and a 'radius' that gets specified
# These inputs are then going to be passed to the actual api calling as they are required fields


import tkinter as tk
from tkinter import ttk

from geopy.geocoders import Nominatim, options
from geopy.exc import GeocoderTimedOut

# Set custom user agent to avoid violating Nominatim's ToS
options.default_user_agent = "my-custom-application"

# List of major US cities (you can expand this list as needed)
us_cities = [
    "New York, NY",
    "Los Angeles, CA",
    "Chicago, IL",
    "Houston, TX",
    "Phoenix, AZ",
    "Philadelphia, PA",
    "San Antonio, TX",
    "San Diego, CA",
    "Dallas, TX",
    "San Jose, CA",
    "Austin, TX",
    "Jacksonville, FL",
    "San Francisco, CA",
    "Indianapolis, IN",
    "Columbus, OH",
    "Fort Worth, TX",
    "Charlotte, NC",
    "Seattle, WA",
    "Denver, CO",
    "Washington, DC",
]


# Function to get latitude and longitude of a city
def get_coordinates(city_name):
    try:
        geolocator = Nominatim(user_agent="my-custom-application")
        location = geolocator.geocode(city_name)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        print("Error: Geocoding service timed out.")
        return None, None


# Function to handle form submission
def submit_form():
    city = city_combobox.get().strip()
    radius = radius_entry.get().strip()

    if city:
        latitude, longitude = get_coordinates(city)
        if latitude is not None and longitude is not None:
            inputs = {
                "city": city,
                "latitude": latitude,
                "longitude": longitude,
                "radius": int(radius) if radius else None,
            }
            print("Input values:")
            print(inputs)
            root.destroy()  # Close the GUI window after submission
        else:
            print(f"Error: Could not find coordinates for '{city}'.")
    else:
        print("Error: Please select a city.")


# Create main window
root = tk.Tk()
root.title("City and Radius Input")

# Create input fields
city_label = ttk.Label(root, text="Select a US City:")
city_label.pack(pady=10)

city_combobox = ttk.Combobox(root, values=us_cities, width=30)
city_combobox.pack()

radius_label = ttk.Label(root, text="Enter a Radius (miles):")
radius_label.pack(pady=10)

radius_entry = ttk.Entry(root, width=10)
radius_entry.pack()

# Create submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Start the GUI main loop
root.mainloop()
