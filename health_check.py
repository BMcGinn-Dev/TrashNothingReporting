import requests
import pandas as pd


# Function to perform health check on a GET API
def health_check(api_url):
    try:
        # Send GET request
        response = requests.get(api_url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful.")

            # Convert JSON response to Python dictionary
            data_dict = response.json()

            # Convert dictionary to Pandas DataFrame
            df = pd.DataFrame([data_dict])

            # Print the DataFrame
            print("Data from API:")
            print(df)

        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Error message:", response.text)

    except requests.exceptions.RequestException as e:
        print("Request failed due to an error:")
        print(e)





# Example usage
if __name__ == "__main__":
    api_url = "https://api.example.com/health"  # Replace with your API endpoint
    health_check(api_url)
