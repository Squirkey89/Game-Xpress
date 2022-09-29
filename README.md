# GameXpress

The GameXpress website is a full-stack Django website built using Python, JavaScript, HTML and CSS. The web application serves as a full-featured B2C e-commerce website for a video game retailer. Customers can purchase a wide selection of games on the site. To name just a few, there are genres like shooting, fighting, football, and racing. The website is simple to use the customer can easlily view products with one click from the home page. The products detail page gives the customer more information about each product and at the bottom of this page the customer can leave a review once they have signed up to the website. The website also contains a favourite page. Customers can add products that they are interested in to their favourites and that list will remain there until they are removed. The customer must be signed in to perform this task. Products can be added to the basket and can be purchased using card payment. The customers can enter a discount code at the basket to get ten percent off their order.An Order confirmation email is sent to the address provided. Users can also stay updated with all the latest and exclusive offers by following on Facebook page and by subscribing to the monthly newsletter.

![amiresponsive](https://user-images.githubusercontent.com/91072896/193037294-1e1f4dd4-a3bf-468a-b4fb-1e85b97c6f78.png)



# Table of Contents
1. [UX](#id-ux)
    * [Strategy](#id-Strategy-plane)
    * [Scope](#id-Scope)
    * [Structure](#id-Structure)
    * [Skeleton](#id-Skeleton)

 

# UX<div id='id-ux'>

The project was broken up into Epics. These Epics roughly translate to apps within the Django project. Each User Story was added to it's relevant Epic, and each User Story was further broken down into smaller tasks.

## Strategy-plane<div id='id-Strategy-plane'>
GameXpress is a business to consumer B2C ecommerce site. It is targeted towards gamers and would appeal to hard core gamers as all products are up to date with the latest software realeased. There is a wide selection of games this is also to attract every type of game from those interested in shooters, sports games or role playing games. The site admin has full control over the site and they can delete and add products as crud is implemented. The website is a easy to use and navigate around. The main strategy was to make the site simple to purchase a product as this is the purpose of an ecommerce site. Within a few clicks the user can make a purchase very easily.

## Scope<div id='id-Scope'>

### User Stories

#### As a Shopper 

* As a shopper I want to be able to add discounts to the checkout so that I can save money when I checkout my products.
* As a shopper I want to be able to leave a review so that I can inform others about my experience with the product.
* As a shopper I want to be able to navigate around the site so that I can easily view the content that I am looking for.
* As a shopper I want to be able to view a list of products in my bag before making payment so that I can see the items and total cost and quantity.
* As a shopper I want to be able to to view an order confirmation after purchase so that I can make sure the order details are all correct.
* As a shopper I want to be able to view the products details so that I can read the product description.
* As a shopper I want to be able to able to view products in their categories so that I can find what I am looking for easily.
* As a shopper I want to be able to review my cart so that I can make adjustments to my cart prior to checkout.
* As a shopper I want to be able to view a list of products so that I can select one to purchase..
* As a shopper I want to be able to add products to a favorites list so that I can easily find these products again when I go back to the website.
* As a shopper I want to be able to complete the payment process quickly and easily so that I can purchase products without any problems.
* As a shopper I want to be able to search for a specific product in the search bar so that I can find what I'm looking for faster.

#### As a User

* As a user I want to be able to easily log in and log out so that I can so I can gain access to my account quickly and hassel free.
* As a user I want to be able to register an account so that I can make purchases and use features on the website.
* As a user I want to be able to view what I had already previously ordered so that I can view a history of my products purchased.
* As a user I want to be able to reset my password if I forget it so that I can regain access to my account.
* As a user I want to be able to receive an email confirmation once I have registered so that I can confirm registration was successful

#### As a Store Owner

* As a store owner I want to be able to add a new product to the store so that I can offer customers the latest products.
* As a store owner I want to be able to delete products so that I can remove products that are out of stock or discontinued.
* As a store owner I want to be able to edit products on the website so that I can make changes to the product details e.g., price if products on sale.

### Epics
 * Set up Django - #1
 * Home app - #2
 * Products app - #3 
 * Basket app - #4 
 * Checkout app - #5 
 * Profiles app - #6 
 * Favourites app - #7 
 * Configure Coupon - #8 
 * Configure Review - #9 
 * Deployment - #10 
 * SEO Implementation- #11 
 * Web Marketing - #12
  
## Structure<div id='id-Structure'>
### Database Schema
Database
The SQLite database was used for the development environment, and the Postgres database for production as an add-on via Heroku. Both are relational databases and work well with the Django framework used for this project.

Data Models
The following models have been used to populate the database and for the site to function as it should:

* Product - the model for the product itself and its details

* Category - the category in which the product is placed

* Review - a model for users to give the product a rating and a review

* Order - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

* OrderLineItem - a model holding the product information for a single product, binding the product model together with the order

* UserProfile - the model storing the users product and order information

* Favourites - the customer has the option to save an item, which will then appear in theirfavourites page once they are signed in.

* Discount Coupon - a model which allows the user to enter a code to get a discount on there basket total.

Schema of models
Below is a schema of the models used in this application, created with Lucidchart

![Database](https://user-images.githubusercontent.com/91072896/193060135-2fbb7cf5-8400-42d5-8cc6-06166b0e375d.png)


# Skeleton<div id='id-Skeleton'>
![GameXpress 1](https://user-images.githubusercontent.com/91072896/193088620-f03a2887-165b-4416-b4b2-26fd77140022.png)
![GameXpress 2](https://user-images.githubusercontent.com/91072896/193088606-a258b217-7082-4077-ba6b-a38a575bf3c8.png)








