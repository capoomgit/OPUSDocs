import requests
import time

# Define global variables for RapidAPI key and host
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'  # Your RapidAPI key
RAPIDAPI_HOST = 'opus-gen02.p.rapidapi.com'  # API host for the Opus service

# Define headers with API key for authentication in requests
headers = {
    'x-rapidapi-key': RAPIDAPI_KEY,  # The API key for accessing the Opus API
    'x-rapidapi-host': RAPIDAPI_HOST  # The host for the Opus API service
}


# Step 1: Process Image - Uploads the image for processing
def process_image(image_path):
    """
    This function uploads an image to the Opus API for processing.
    It uses the provided file path to send the image to the API, which processes it
    and returns a job unique identifier (job_uid).
    """
    url = f"https://{RAPIDAPI_HOST}/process-image"  # The URL for processing the image
    files = {
        'file1': (image_path.split("/")[-1], open(image_path, 'rb'), 'image/jpeg')
        # Open the image in binary mode and send it
    }

    # Send the image to the Opus API using a POST request
    response = requests.post(url, headers=headers, files=files)
    data = response.json()  # Parse the JSON response from the API
    job_uid = data['job_uid']  # Extract the job UID from the response

    print(f"Image processing job queued. Job UID: {job_uid}")
    return job_uid  # Return the job UID to be used in subsequent steps


# Step 2: Poll Job Status - Checks the processing status of the uploaded image
def poll_job_status(job_uid):
    """
    This function polls the status of the image processing job.
    It checks if the job has completed or failed. If not, it keeps polling until
    the job is finished or failed.
    """
    url = f"https://{RAPIDAPI_HOST}/job_result/{job_uid}"  # URL to check job status

    while True:
        response = requests.get(url, headers=headers)  # Send a GET request to check job status
        data = response.json()  # Parse the JSON response

        if data['status'] == 'COMPLETED':
            print("Image processing completed successfully.")
            return data  # Return the completed job data if status is 'COMPLETED'
        elif data['status'] == 'FAILED':
            print("Image processing failed. Check for errors.")
            return None  # Return None if the job failed

        print("Waiting for processing to complete...")
        time.sleep(5)  # Poll every 5 seconds to check the job status


# Step 3: Get MP4 Preview URL (Optional) - Retrieves the MP4 preview URL if available
def get_mp4_preview(data):
    """
    This function checks the completed job data for an MP4 preview URL.
    If the processing was successful, it will extract and return the URL of the MP4 preview.
    """
    if data and data['status'] == 'COMPLETED':  # Check if processing is completed
        mp4_url = data['urls'][0]['url']  # Extract the first URL assuming it's the MP4 preview
        print(f"MP4 preview URL: {mp4_url}")
        return mp4_url  # Return the MP4 URL
    else:
        print("No MP4 URL found or processing failed.")
        return None  # Return None if no MP4 URL is found or processing failed


# Step 4: Extract GLB - Requests the extraction of the GLB file from the processed image
def extract_glb(job_uid):
    """
    This function requests the extraction of a GLB file from the processed image.
    It sends a POST request to the Opus API to initiate the GLB extraction process.
    """
    url = f"https://{RAPIDAPI_HOST}/extract-glb"  # URL to request GLB extraction
    querystring = {"job_uid": job_uid}  # Pass the job UID as a query parameter
    payload = {}  # No payload is needed for this request

    # Send the POST request to initiate the GLB extraction
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    data = response.json()  # Parse the JSON response
    glb_job_uid = data['job_uid']  # Extract the job UID for the GLB extraction

    print(f"GLB extraction job queued. Job UID: {glb_job_uid}")
    return glb_job_uid  # Return the GLB job UID to track its progress


# Step 5: Poll GLB Extraction Job Status - Polls the GLB extraction job until completed
def poll_glb_status(glb_job_uid):
    """
    This function polls the status of the GLB extraction job.
    It checks whether the GLB extraction has completed and returns the GLB URL when available.
    """
    url = f"https://{RAPIDAPI_HOST}/job_result/{glb_job_uid}"  # URL to check GLB job status

    while True:
        response = requests.get(url, headers=headers)  # Send a GET request to check the GLB job status
        data = response.json()  # Parse the JSON response

        if data['status'] == 'COMPLETED':
            urls = data.get("urls", [])  # Get the list of URLs from the response
            for url_entry in urls:
                # Check for a GLB extension and ensure the URL exists
                if url_entry.get("extension") == "glb" and url_entry.get("url"):
                    glb_url = url_entry.get("url")
                    print(f"GLB extraction completed. GLB URL: {glb_url}")
                    return glb_url  # Return the GLB URL when found
        elif data['status'] == 'FAILED':
            print("GLB extraction failed. Check for errors.")
            return None  # Return None if the GLB extraction failed

        print("Waiting for GLB extraction to complete...")
        time.sleep(5)  # Poll every 5 seconds


# Step 6: Extract Gaussian - Requests the extraction of the Gaussian data (PLY format)
def extract_gaussian(job_uid):
    """
    This function requests the extraction of Gaussian data in PLY format.
    It sends a POST request to the Opus API to initiate the Gaussian extraction process.
    """
    url = f"https://{RAPIDAPI_HOST}/extract-gaussian"  # URL to request Gaussian extraction
    querystring = {"job_uid": job_uid}  # Pass the job UID as a query parameter
    payload = {}  # No payload is needed for this request

    # Send the POST request to initiate the Gaussian extraction
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    data = response.json()  # Parse the JSON response
    gaussian_job_uid = data['job_uid']  # Extract the job UID for the Gaussian extraction

    print(f"Gaussian extraction job queued. Job UID: {gaussian_job_uid}")
    return gaussian_job_uid  # Return the Gaussian job UID to track its progress


# Step 7: Poll Gaussian Extraction Job Status - Polls the Gaussian extraction job until completed
def poll_gaussian_status(gaussian_job_uid):
    """
    This function polls the status of the Gaussian extraction job.
    It checks whether the Gaussian extraction has completed and returns the PLY URL when available.
    """
    url = f"https://{RAPIDAPI_HOST}/job_result/{gaussian_job_uid}"  # URL to check Gaussian job status

    while True:
        response = requests.get(url, headers=headers)  # Send a GET request to check the Gaussian job status
        data = response.json()  # Parse the JSON response

        if data['status'] == 'COMPLETED':
            urls = data.get("urls", [])  # Get the list of URLs from the response
            for url_entry in urls:
                # Check for a PLY extension and ensure the URL exists
                if url_entry.get("extension") == "ply" and url_entry.get("url"):
                    ply_url = url_entry.get("url")
                    print(f"Gaussian extraction completed. PLY URL: {ply_url}")
                    return ply_url  # Return the PLY URL when found
        elif data['status'] == 'FAILED':
            print("Gaussian extraction failed. Check for errors.")
            return None  # Return None if the Gaussian extraction failed

        print("Waiting for Gaussian extraction to complete...")
        time.sleep(5)  # Poll every 5 seconds


# Main function to run the entire flow
def main():
    """
    This is the main function that runs the entire process:
    1. Uploads the image to the Opus API for processing.
    2. Polls for the job status to check when it's complete.
    3. Optionally extracts and checks the MP4, GLB, or Gaussian files.

    Note: We need to ensure that the image processing is completed before we call the extraction functions.
          Additionally, after calling either GLB or Gaussian extraction, we need to wait for that specific
          process to complete before proceeding to the next one.
    """
    image_path = "/Users/gihadsohsah/specta-chair-red-SP-RE-view1-800x800.jpg"  # Path to the image for processing

    # Step 1: Process the image and get the job UID
    job_uid = process_image(image_path)

    # Step 2: Poll for the image processing job status to ensure it is completed before continuing
    data = poll_job_status(job_uid)

    # Step 3: Get the MP4 preview URL (optional)
    mp4_url = get_mp4_preview(data)

    # Step 4: If preview is satisfactory, proceed with extracting GLB
    if mp4_url:
        extract_glb(job_uid)  # Initiate GLB extraction
        glb_url = poll_glb_status(job_uid)  # Poll for the GLB URL

    # Step 5: If needed, extract Gaussian data (PLY)
    if mp4_url:  # You can also extract Gaussian data if required
        extract_gaussian(job_uid)  # Initiate Gaussian extraction
        gaussian_url = poll_gaussian_status(job_uid)  # Poll for the PLY URL


# Execute the main function
if __name__ == "__main__":
    main()
