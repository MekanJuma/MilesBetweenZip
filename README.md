# MilesBetweenZip: ZIP Code Location & Distance Analyzer
MilesBetweenZip is a Python-based program that allows users to determine the city and state details associated with ZIP codes, as well as calculate the driving distance between two given ZIP codes using the Google Maps API.

# Features
- Fetch city and state details for a given ZIP code.
- Calculate accurate driving distances between two ZIP codes using the Google Maps API.
- Designed for easy integration into applications requiring ZIP-based location data and route planning.

# Pre-requisites
Before you start using MilesBetweenZip, you need to obtain a Google Maps API key. The driving distance calculation relies on the Google Maps API to provide accurate results.

**1. Obtaining a Google Maps API Key:**
  - Visit the [Google Cloud Console](https://cloud.google.com/console/google/maps-apis).
  - Click the **Get Started** button and enable the Google Maps Directions API.
  - Create a new project and set up the billing (Note: While Google Maps is a paid service, there's a free tier that you can often stay within based on your usage).
  - Once set up, you'll receive an API key. Make sure to securely store this key and never commit it directly to your code or public repositories.

# Installation

1. Clone the Repository:
```
git clone https://github.com/MekanJuma/MilesBetweenZip.git
cd MilesBetweenZip
```
2. Set up a Virtual Environment (Optional but Recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install Dependencies:
```
pip install -r requirements.txt
```

**Happy coding guys :)**
