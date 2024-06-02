import requests
from datetime import date

#I have created and called this empty_files function to make sure the files are emptied everytime we run the project for the assignment purpose /
def reset_files():
    with open("my_basket.txt", "w") as basket_file:
        basket_file.write('Your basket is empty! Re-run the program and select browse items to find makeup products and add them to your basket')
    with open("my_wishlist.txt", "w") as wishlist_file:
        wishlist_file.write('Your wishlist is empty! Re-run the program and select browse items to find makeup products and add them to your wishlist')


reset_files()

options = {
    1: "Browse makeup products",
    2: "View basket",
    3: "View wishlist"
}

endpoint = "http://makeup-api.herokuapp.com/api/v1/products.json?"

product_types = ["blush", "bronzer", "eyebrow", "eyeliner", "eyeshadow", "foundation", "lip liner", "lipstick",
                 "mascara", "nail polish"]

#this will fetch the brands data which I have stored in the available_brands file. This will allow us to simply update that file in case we want to add some more available brands or delete some
with open("available_brands.txt", "r") as brands:
    brand_data = brands.read()
    brand_list = brand_data.split("\n")

input("Hi! Welcome to CFG Beauty! Press enter to start")


def give_options():
    return input(
        f"Choose one of the following options:\n1:{options[1]}\n2:{options[2]}\n3:{options[3]}\nType the option number here: ")


user_choice = give_options()

option_choice = options[int(user_choice)]


#created a functions to display a list's item on multiline or on the same line with a separator that can be a "-", "," or "/" for example. This function has a return that makes the code reusable
def display_list(given_list, multiline_option, separator=None):
    result = ""
    for x in given_list:
        if multiline_option == True:
            result += f"{x}\n"
        elif multiline_option == False:
            result += f"{x} {separator} "
            if given_list.index(x) > 0 and given_list.index(
                    x) % 5 == 0:  #for user readability I will display only 5 brands per line
                result += "\n"

    return result


#Created handle_browse_idem function for better readability of the conditional statements
def handle_browse_item():
    brand_choice = input(
        f"Are you looking for products from a specific Brand? If so, type the brand name and press enter. Please make sure you select one of our available brands from the list below:\n{display_list(brand_list, False, ',')}\nIf not, just press enter: ").lower()

    product_choice = input(
        f"What product type are you looking for today? Select from the following:\n{display_list(product_types, True)}\nType your choice here: ").lower()
    # could make a list of product type and if the input is not on the list displays error message

    user_budget = input("Please enter your budget: ")

    response = requests.get(
        f"{endpoint}brand={brand_choice}&product_type={product_choice}&price_greater_than=0&price_less_than={user_budget}")

    data = response.json()

    if len(data) == 0:
        print("Sorry, no items found. Please re-run the program and try again")
        exit()
    # # we are exiting the program if no items are found
    else:

        with open("search_result.txt", "w") as search_result:
            search_result.write(f"SEARCH RESULTS FOR {product_choice.upper()}\n\n")

            for item in data:
               search_result.write(f"Item number: {item['id']}\n"
                                f"Brand: {item['brand']}\n"
                                f"Name: {item['name']}\n"
                                f"Description: {item['description']}\n"
                                f"Tags: {display_list(item['tag_list'], False, '/')}\n"
                                f"Price: ${item['price']}\n"
                                f"Added on: {date.fromisoformat(item['created_at'][0:10])}\n ---------- \n\n") #Using date from datetime module to format the created at date

        print(f"Search results for {product_choice}:\n")
        print(f"Item number:{data[0]['id']}\n{data[0]['brand'].capitalize()}\n{data[0]['name']}\nDescription: {data[0]['description'][0:30]}...\n${data[0]['price']}\n------------")
        print(f"View more\n------------\n\nOpen the search_result.txt file to see more items and check the full results of your search!")
    # inserted "---" for better user visualisation in the console
    # for the Item description I have decided to use the string slicing to give a quick intro of the description as the user can then open the search_results.txt file to see more details including the full description

    selected_items = input(
        "Has anything caught your eye?\nIf so, enter the item numbers of the products you want to add to your basket/wishlist separated by a comma(ex. 1,4,65...)\nOtherwise, re-run the program to browse new items: ").split(
        ",")

    if len(selected_items) > 0 and selected_items[0] != "": # this will check that the user has actually selected some items and we don't use and empty list
            save_option = input(
                "Would you like to save the selected item(s) in your basket or wishlist? Type basket or wishlist: ").lower()

            with open(f"my_{save_option}.txt", "w") as saved_items_file:
                saved_items_file.write(f"MY {save_option.upper()}\n----------\n")

                for item in data:

                    if str(item['id']) in selected_items:
                        saved_items_file.write(f"Item number: {item['id']}\n"
                                               f"Brand: {item['brand']}\n"
                                               f"Name: {item['name']}\n"
                                               f"Description: {item['description']}\n"
                                               f"Tags: {display_list(item['tag_list'], False)}\n"
                                               f"Price: £{item['price']}\n\n ---------- \n\n")
            print(f"Amazing choice! Check your {save_option}.txt file to see the items you saved in your {save_option}")
    else:
        print("You haven't selected any items, please re-run the program and try again")
        return




if option_choice == options[1]:
    handle_browse_item()

elif option_choice == options[2]:
    with open("my_basket.txt", "r") as basket_file:
        basket_data = basket_file.read()

        print(basket_data)

#If the user selects option 2 or 3 as soon as they run the program therefore before adding any items to the basket/wishlist - the program will run and print the content of the basket or wishlist file which says they are still empty
elif option_choice == options[3]:
    with open("my_wishlist.txt", "r") as wishlist_file:
        wishlist_data = wishlist_file.read()

        print(wishlist_data)
else:
    print("The entered number doesn't match any of the existing options. Please re-run the program and try again!")

#Find a way to start again at any point in the console app
