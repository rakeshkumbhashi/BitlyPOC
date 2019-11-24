# BitlyPOC
POC using Flask Rest API and MongoDB for URL shortener sample

- Supports two routes: URLGen and URL Redirector

URLGen:
- Request for a long URL to shorten received via POST request (URLGEN)
  Uses base62 encoding to shorten URL and save same into MongoDB
- User can perform a GET request to find the long URL associated with a short URL

URLRedirector:
- User can perform a GET request to auto redirect User to long URL given the short URL
  
