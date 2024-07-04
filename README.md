# CFG Beauty - Makeup Shopping Console Application

The CFG Beauty is a console application that helps users browse makeup products and add them to their basket or wishlist through a simple command-line interface

### Prequisite: 
##### Python3.x

### To run the program, you will need to install:
requests library running the command
```sh
pip install requests
```

### Ensure that the following files are in the same directory as the script:
- my_basket.txt
- my_wishlist.txt
- available_brands.txt

### The Makeup API
The Makeup API is a RESTful service that allows users to search for makeup products by various criteria such as brand, product type, price, and tags 

Info: http://makeup-api.herokuapp.com/

##### API endpoint used: 

http://makeup-api.herokuapp.com/api/v1/products.json

##### Type of request: GET 
Response format: .json (using the .json() method to parse the results data I got from the API)

This API enables users to filter products by parameters like brand, product category, price range, and ratings.


## How to use CFG Beauty:
 Run the script - 
 Choose an option between browsing makeup products, view basket and view wishlist 

 Browse product - 
 You can filter products by brand, product type (e.g.Blush, Bronzer, Mascara...)
 Enter your budget
 A list of items corresponding to your selected parameters will be fetched from the API and stored in a new search_results.txt file 
 Add items to your basket or wishlist by entering item numbers

### Happy Path:
For this project I have followed a happy path first approach, assuming the user will follow the correct instructions as promped. After that, I have implemented some error handling in case the user selected an unexistent option or didn't selected any items

### Key points:
- Reset Files: Ensures my_basket.txt and my_wishlist.txt are empty at the start of each run to make sure the user can add their items while running the app
- Browse Products: Allows users to browse makeup products by brand, type, and budget
- View Basket and Wishlist: Users can view the items they've added to their basket or wishlist

### Points for improvement:
While working on the CFG Beauty app, I have been taking notes for points that would improve the app for a better user experience, such as:
- Add price filter for greater than a specified amount
- Unfortunately, the data for the items' rating was poor but it would be ideal to add a feature to filter items by ratings
- Many items had a price of 0, which is why I have added the price_greater_than 0 as parameter in my get request to the API
- Use a currency converter library to handle different currencies (all prices are currently in CAD)
- Add an option to move items from the wishlist to the basket
- Provide an option to browse again and keep adding items to the basket/wishlist. Allowing repetition of the script without losing the data stored in the basket/wishlist files
- Option to remove items from the basket once purchased 