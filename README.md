# Info_Gathering_Tool

## 🔍 Overview

**Info_Gathering_Tool** is a Python-based command-line utility designed for ethical hacking and reconnaissance. It retrieves key metadata about a target domain, including IP address, HTTP headers, and geographic information by using the `ipinfo.io` API and native Python libraries.

## 🚀 Features

- Fetches HTTP response headers of a given website.
- Resolves domain names to their corresponding IP addresses.
- Retrieves geolocation data (city, region, country, coordinates).
- Identifies the organization associated with the IP address.

## 🛠 Technologies Used

- Python
- `requests` for HTTP requests
- `socket` for DNS resolution
- `json` for API response handling

## ⚙️ How to Use

### 📦 Requirements
Install Python packages using pip if not already installed:

pip install requests

▶️**Run the Tool**

python code.py example.com

📌 **Example Output**

{'Server': 'cloudflare', ...}  # HTTP headers
The IP address of example.com is: 93.184.216.34

Location: 37.4056,-122.0775
Region: California
City: Mountain View
Country: US
Organization: AS15169 Google LLC

⚠️ **Disclaimer**
This tool is intended for educational and ethical use only. Do not use it on websites or domains you do not own or have permission to analyze.

📃 **License**
This project is licensed under the MIT License.
