# Opus API Integration - Python Example

This repository contains a Python script (`test.py`) [here](./test.py). that demonstrates how to integrate with the Opus API for processing images, extracting GLB, and Gaussian (PLY) files. The script is designed to serve as a guideline for integrating the Opus API into your workflow.

## Prerequisites

- Python 3.x
- `requests` library (can be installed using `pip install requests`)

## Overview

The script demonstrates the following key operations:
1. **Image Processing**: Uploads an image to the Opus API for processing.
2. **Polling for Completion**: Continuously checks the status of the image processing job until it is completed.
3. **MP4 Preview**: Optionally retrieves an MP4 preview of the processed image.
4. **GLB and Gaussian Extraction**: Optionally extracts the GLB or Gaussian (PLY) files from the processed image. The extraction process is completed sequentially, ensuring that one extraction is finished before the next begins.

### Key Notes:
- **Image Processing Completion**: The image processing must be completed before proceeding with extracting either GLB or PLY files.
- **Sequential Extraction**: After initiating the GLB or Gaussian (PLY) extraction, the script waits for the respective extraction to finish before proceeding with the next extraction process.

## Key Functions

### 1. `process_image(image_path)`
Uploads the image to the Opus API and returns a unique job ID for processing.

**Parameters**:
- `image_path` (str): The path to the image you want to upload.

**Returns**:
- `job_uid` (str): A unique identifier for the image processing job.

### 2. `poll_job_status(job_uid)`
Polls the Opus API to check the status of the image processing job.

**Parameters**:
- `job_uid` (str): The unique job ID for the image processing job.

**Returns**:
- `data` (dict): The processed job data if the job is completed.

### 3. `get_mp4_preview(data)`
Retrieves the MP4 preview URL from the processed image (optional).

**Parameters**:
- `data` (dict): The processed job data returned by `poll_job_status`.

**Returns**:
- `mp4_url` (str): The URL for the MP4 preview.

### 4. `extract_glb(job_uid)`
Requests the Opus API to extract a GLB file from the processed image.

**Parameters**:
- `job_uid` (str): The unique job ID for the image processing job.

**Returns**:
- `glb_job_uid` (str): A unique identifier for the GLB extraction job.

### 5. `poll_glb_status(glb_job_uid)`
Polls the Opus API to check the status of the GLB extraction job.

**Parameters**:
- `glb_job_uid` (str): The unique job ID for the GLB extraction job.

**Returns**:
- `glb_url` (str): The URL for the extracted GLB file.

### 6. `extract_gaussian(job_uid)`
Requests the Opus API to extract a Gaussian (PLY) file from the processed image.

**Parameters**:
- `job_uid` (str): The unique job ID for the image processing job.

**Returns**:
- `gaussian_job_uid` (str): A unique identifier for the Gaussian extraction job.

### 7. `poll_gaussian_status(gaussian_job_uid)`
Polls the Opus API to check the status of the Gaussian (PLY) extraction job.

**Parameters**:
- `gaussian_job_uid` (str): The unique job ID for the Gaussian extraction job.

**Returns**:
- `ply_url` (str): The URL for the extracted Gaussian (PLY) file.

## Workflow

1. **Process Image**: The script starts by uploading an image using the `process_image()` function, which returns a `job_uid`.
2. **Polling Image Status**: The script then calls `poll_job_status()` to wait until the image processing is completed.
3. **MP4 Preview (Optional)**: If needed, `get_mp4_preview()` retrieves a preview of the processed image in MP4 format.
4. **Extract GLB (Optional)**: If the preview is satisfactory, the script proceeds with extracting a GLB file using `extract_glb()` and checks the status using `poll_glb_status()`.
5. **Extract Gaussian (Optional)**: If necessary, the script can also extract Gaussian (PLY) files using `extract_gaussian()` and checks the status using `poll_gaussian_status()`.

## Important Notes:
- **Order of Execution**: Ensure that the image processing is completed before extracting GLB or Gaussian files. Once you initiate any of these extractions, wait for that extraction to finish before starting another.
- **Polling Interval**: The script polls the Opus API every 5 seconds to check job status. This interval can be adjusted based on your needs.

## Usage

To use this script, download the `test.py` file from the repository and run it in your local Python environment.

**Note**: Ensure that you have updated the API keys and paths as needed.

## Conclusion

This Python script serves as a basic integration guideline for working with the Opus API. It ensures the proper sequence of operations and provides the flexibility to handle both GLB and Gaussian extractions. Feel free to adapt the code for your specific use case.

You can find the Python script [here](./test.py).
