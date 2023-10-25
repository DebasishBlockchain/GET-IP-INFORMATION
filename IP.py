import requests

# Replace 'your_api_token' with your actual API token if required by the service
api_token = '5a654c91ea3824'
ip_address = input("Enter an IP address: ")

# Construct the URL for the IP geolocation API
url = f'https://ipinfo.io/{ip_address}/json?token={api_token}'

try:
    response = requests.get(url)
    data = response.json()

    if 'loc' in data:
        location = data['loc'].split(',')
        latitude, longitude = location
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')

        print(f'IP Address: {ip_address}')
        print(f'City: {city}')
        print(f'Region: {region}')
        print(f'Country: {country}')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
    else:
        print("Location data not found for the given IP address.")

except requests.RequestException as e:
    print(f"An error occurred while fetching data: {e}")
