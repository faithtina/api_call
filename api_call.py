import requests

# Define the API endpoint URLs
upload_url = 'https://api.example.com/upload'
download_url = 'https://api.example.com/download'

# Function to upload data to the API
def upload_data(file_path):
    try:
        # Open and read the file
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(upload_url, files=files)

            if response.status_code == 200:
                print("Upload successful!")
            else:
                print(f"Upload failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error uploading data: {str(e)}")

# Function to download data from the API
def download_data(file_id):
    try:
        response = requests.get(f'{download_url}/{file_id}')

        if response.status_code == 200:
            # Save the downloaded data to a file
            with open(f'downloaded_file_{file_id}.txt', 'wb') as file:
                file.write(response.content)
            print("Download successful!")
        else:
            print(f"Download failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading data: {str(e)}")

# Example usage
if __name__ == "__main__":
    upload_data('file_to_upload.txt')  # Replace with your file path
    download_data('123')  # Replace with the specific file ID you want to download
