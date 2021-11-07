# TNScraper
A web scraper designed to take the property name, type of property, amenities, bedrooms and bathrooms from an AirBNB listing


To begin with I decided to use Python for this task as I feel keeping code simple, clean and self-explanatory is always good practice. Now as AirBNB listings contain dozens
if not hundreds of elements contained within their HTML page I found it best to first identify the elements which contained the information set in the requirements, now as AirBNB
seemed to use some Javascript frameworks to randomly generate their element IDs for individual listings this code would need to have the identifiers tweaked when running against
seperate listings. 

The scraper code is meant to pick out any text found within the chosen elements, selected via their class id and then format them into a JSON object, then store it into a text file for future use, the reason I chose to do this as opposed to a normal print out to console is so the result can be reused and stored in a database or utilised by an API hence the JSON format for ease of use.
