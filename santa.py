import requests
from bs4 import BeautifulSoup

def get_santa_tracker_data():
    # The URL of the NORAD Santa Tracker page
    url = "https://www.noradsanta.org/"

    try:
        # Send a GET request to fetch the HTML024 content of the page
        response = requests.get(url)
        
        # If the request was successful (status code 200)
        if response.status_code == 200:
            print("Page fetched successfully!")

            # Parse the page content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Example: Attempting to find the Santa location and gifts delivered (replace with actual HTML structure)
            # We need to inspect the page source and find the correct classes or IDs for the elements
            
            # Find Santa's location (assuming it's in a div with a class 'santa-location')
            location_element = soup.find('div', class_='santa-location')  # Replace with actual class
            if location_element:
                location = location_element.text.strip()
            else:
                location = "Location not found"

            # Find the number of gifts delivered (assuming it's in a div with a class 'gifts-delivered')
            gifts_element = soup.find('div', class_='gifts-delivered')  # Replace with actual class
            if gifts_element:
                gifts_delivered = gifts_element.text.strip()
            else:
                gifts_delivered = "Gifts data not found"

            # Print the extracted data
            print(f"Santa's Current Location: {location}")
            print(f"Gifts Delivered: {gifts_delivered}")
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to get the data
get_santa_tracker_data()
