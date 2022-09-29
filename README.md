# GameXpress

The GameXpress website is a full-stack Django website built using Python, JavaScript, HTML and CSS. The web application serves as a full-featured B2C e-commerce website for a video game retailer. Customers can purchase a wide selection of games on the site. To name just a few, there are genres like shooting, fighting, football, and racing. The website is simple to use the customer can easlily view products with one click from the home page. The products detail page gives the customer more information about each product and at the bottom of this page the customer can leave a review once they have signed up to the website. The website also contains a favourite page. Customers can add products that they are interested in to their favourites and that list will remain there until they are removed. The customer must be signed in to perform this task. Products can be added to the basket and can be purchased using card payment. The customers can enter a discount code at the basket to get ten percent off their order.An Order confirmation email is sent to the address provided. Users can also stay updated with all the latest and exclusive offers by following on Facebook page and by subscribing to the monthly newsletter.

![amiresponsive](https://user-images.githubusercontent.com/91072896/193037294-1e1f4dd4-a3bf-468a-b4fb-1e85b97c6f78.png)



# Table of Contents
1. [UX](#id-ux)
    * [Strategy](#id-Strategy-plane)
    * [Scope](#id-Scope)
    * [Structure](#id-Structure)
    * [Skeleton](#id-Skeleton)
2. [Features](#id-features)
3. [Features to Implement in the future](#id-implement)
4. [Testing](#id-testing)
5. [Marketing](#id-marketing)
5. [SEO](#id-seo)
6. 
 

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

## Wireframes
  Balsamiq was used to create wireframes fot this project.
[Wireframes 1](https://user-images.githubusercontent.com/91072896/193088620-f03a2887-165b-4416-b4b2-26fd77140022.png)
[Wireframes 2](https://user-images.githubusercontent.com/91072896/193088606-a258b217-7082-4077-ba6b-a38a575bf3c8.png)



# Features<div id='id-features'>

## Navigation-bar<div id='id-nav'>
The navigation bar is at the top of the website. This includes the website name which appears at the left of the nav bar. It also includes links to different categories that the user can visit. Theres a link to the basket, user profile and favourites at the top right of the navigation bar. There is also a search box in the center which can be used to search products. The navbar links change format to hamburger format if the website is viewed on smaller devices.&nbsp;
![nav-bar](https://user-images.githubusercontent.com/91072896/193100438-caf4b61e-37d0-46eb-861e-a3346a62570b.png)


## Home<div id='id-home'>
The home page features three images on a carousel. These images show the customer the type of products to expect from the website. The user has the option to choose netween the three with a link to three different categories.&nbsp;
![Home](https://user-images.githubusercontent.com/91072896/193098334-0217301e-1edb-49ba-a348-c3eb3845c55b.png)

## Products<div id='id-products'>
The products page displays the summary of each product the website sells.The products page contains product image, product name, category, price and favourites button. Each product can be clicked on to view the product in detail on another page. Products can also be filtered via different categories by rating price and ascending or descending order.&nbsp;
![products](https://user-images.githubusercontent.com/91072896/193101055-05501abc-6e5d-43d4-9ea7-75d21792df35.png)

## Product-detail<div id='id-product-detail'>
The product detail page shows information of the product including; product title, price, category, and product description. The user can add products to their basket before checkout. The user can also add products to their favourites list. Below the product detail there is an area for submit and read users reviews.&nbsp;
![product detail](https://user-images.githubusercontent.com/91072896/193102028-91f2e88a-4b51-4a8c-b07a-95b602c8b46b.png)
![review](https://user-images.githubusercontent.com/91072896/193103476-55fbed49-a4d6-418b-aa1a-c556363157dd.png)

## Basket<div id='id-basket'>
Once the user goes to the basket page they can review there order. Thre is an option to increment or decrement quantity or remove the item completely. There is a discount code at the bottom of the page and a banner above the page with a valid code. When the user types this into the discount box they will receive 10% off there order. They will get the amount deducted from their total.&nbsp;
![Basket](https://user-images.githubusercontent.com/91072896/193106655-8f9b0b0e-34c8-44ed-a46f-c53609483c6b.png)

## Checkout<div id='id-checkout'>
When the user is ready to proceed to the checkout page after selecting their choice of products. They will have to fill in their billing and delivery details before they confirm the purchase has been made. The user is signed up has the option to save their details for future purchases. This makes the experience much faster and a better experience for the customer.&nbsp;

## Checkout-success<div id='id-checkout-success'>
After users have placed their order, an order confirmation page is displayed with the summary of the order placed including; product details, personal information, order number and the email that is used to send the order confirmation to.&nbsp;
![checkout success](https://user-images.githubusercontent.com/91072896/193108200-716d8a02-0a42-4118-a4ea-82d5f918e3e5.png)

## User-Profile<div id='id-user-profile'>
Registered users have an option to view their profile. This page is where the customer sets their personal information so this information is saved when the customer wants to go back to make a purchase. This also has a list of the users order history which they can view at any time.
![User profile](https://user-images.githubusercontent.com/91072896/193109731-519d3e92-7165-4609-86e3-868fde9210fd.png)

## Favourites<div id='id-favourites'>
The favourites page is a page only available to users that have registered an account. These users have an option to add products to their favourites. The user can add a product that they may want to buy sometime in the future. The user can add as many items as they would like and they can aslo remove these products. 
![Favourites](https://user-images.githubusercontent.com/91072896/193110282-605f094d-057f-4b2e-80e0-2c88717051ec.png)


# Features to Implement in the future<div id='id-implement'>
There are a lot of improvements I would make and features I could add to make the site better.
  * The coupon code can currently be used by a customer as many times as they would like. I would change this to one code per customer. When creating the coupon I was going to make an expiry but decided against it.
  * The favourites app can do almost everything but I would implement an add to basket buttn. This would allow the customer to easily purchase the item if its in their favourites.

  # Testing<div id='id-testing'>
  During my project I tested my user stories as I was going through my project. I gave each user story an acceptance criteria and tasks and once I felt these were met I moved them to done.

  ### USER STORY: Products 1

    As a shopper I want to be able to view a list of products so that I can select one to purchase.

    Acceptance Criteria:
    Given the user navigates to the products on the site. When they view the list of all products that are available to purchase. Then the user can choose what they would like to purchase.

    Tasks
    * Good layout/Navigation
    * High quality images
    * Good SEO implementation

  ### USER STORY: Review 2
    As a shopper I want to be able to leave a review so that I can inform others about my experience with the product.

    Acceptance Criteria
    Given that the user will view the product detail to find more information about the ptoduct. When the user clicks on the product they can then see the reviews left by others

    Tasks
    * Add Review Model
    * Create review form in product detail template

  ### USER STORY: Navigation 3
    As a shopper I want to be able to navigate around the site so that I can easily view the content that I am looking for.#

    Acceptance Criteria
    Given that there is a lot of content on the site. When the user visits the website, they will find a responsive navigation bar and an easy to use navigation system. Then they can then click on the links to direct them to the pages they are looking for.

    Tasks
    * Well designed navbar
    * Responsive on all devices
    * Bootstrap and Hamburger dropdown menu

  ### USER STORY: Search 4
    As a shopper I want to be able to search for a specific product in the search bar so that I can find what I'm looking for faster

    Acceptance Criteria
    Given that the user will want to look for a specific product When they enter the name of the product in the search bar. Then the website searches all products on the website to see if a match is found.

    Tasks
    * Add code to product views to perform this function 

  ### USER STORY: Search 5
    As a shopper I want to be able to add products to a favorites list so that I can easily find these products again when I go back to the website

    Acceptance Criteria
    Given that the user sees a product that they like. The user can click on the product and add this to there favourites. Then when the user goes to the favourites page a list of the users favourite products will appear on this page.

    Tasks
    * Create custom favourite model
    * Link up with views and urls
    * Create favourites template

  ### USER STORY: Adjustments to basket 6
    As a shopper I want to be able to review my cart so that I can make adjustments to my basket prior to checkout

    Acceptance Criteria
    Given that the customer can make adjustments to the products that they have in their bag. When they get to the checkout they can make theses adjustments. Then the user can remove individual products or increase or decrease the quantity.

    Tasks
    * Create adjust bag view
    * Add html to template
    * Connect URL's

  ### USER STORY: Discounts 7

    As a shopper I want to be able to add discounts to the checkout so that I can save money when I checkout my products

    Acceptance Criteria
    Given that there is a newsletter at the footer of the website. When the user enters there email address in the form. Then they will receive discount which can save them money at the checkout

    Tasks
    * Create coupon view
    * Add to html in checkout

  ### USER STORY: Payment 8

    As a shopper I want to be able to complete the payment process quickly and easily so that I can purchase products without any problems

    Acceptance Criteria
    Given the user wants to puchase products from the site. When the user adds products to the bag and navigates to the checkout. Then the users can fill out the credit card details and complete the payment.

    Tasks
    * Create a Stripe account
    * Add stripe public and private keys to environment variables
    * Add stripe code to checkout.html

  ### USER STORY: Order Confirmation 9

    As a shopper I want to be able to to view an order confirmation after purchase so that I can make sure the order details are all correct

    Acceptance Criteria
    Given that the shopper wants makes a purchase and would confirmation of this. When the customer enters all their details and processes the payment. Then the customer will be transferred to their profile page. This is where they will see confirmation of the order.

    Tasks
    * Write code to display order confirmation for authenticated users
    * Create order mode

  ### USER STORY: Newsletter 10

    As a shopper I want to be able to sign up for the mail list so that I can be contacted when new releases and the latest offers are available

    Acceptance Criteria
    Given that there is a newsletter aviable to sign up to on the footer of the site. When the customer enters their email address on the for. Then they will recieve offers and discounts.

    Tasks
    * Sign up to mailchimp
    * Add html to base template
    * Connect URL's

  ### USER STORY: Categories 11

    As a shopper I want to be able to able to view products in their categories so that I can find what I am looking for easily

    Acceptance Criteria
    Given that the user will want to find their specific product. When they click on the categories tab on the navbar this will then bring up the different categories, making it easier for the user to find what they are loking for.

    Tasks
    * Create categories tab in navbar
    * Connect URL's
    * Create category model

  ### USER STORY: Registration 12

    As a user I want to be able to register an account so that I can make purchases and use features on the website

    Acceptance Criteria
    Given that this is a new user, when they they fill out the short registration form, then they are successfully registered and able to log in with chosen credentials.

    Tasks
    * Install django-allauth
    * Build Registration Template
    * Test functionality

  ### USER STORY: Order History 13

    As a user I want to be able to view what I had already previously ordered so that I can view a history of my products purchased

    Acceptance Criteria
    Given that the user has already made a purchase on the website. When the customer logs in to there account and views there profile. Then the user can view a history of the products which they ordered.

    Tasks
    * Write code to display order history for authenticated users
    * From users profile links to each order made

  ### USER STORY: Registration confirmation 14

    As a user I want to be able to receive an email confirmation once I have registered so that I can confirm registration was successful

    Acceptance Criteria
    Given that the user has completed the registration form and provided their email address. The user will instantly receive an email confirming successful registration

    Tasks
    * Set up emails with gmail
    * Add code to send emails
    * Install django-allauth

  ### USER STORY: Log In/Out 15

    As a user I want to be able to easily log in and log out so that I can so I can gain access to my account quickly and hassel free

    Acceptance Criteria
    Given that the user is registered, if they go to the log in page and enter username and password and click on Log in. The data the user entered will allow them to log into their associated account. While clicking logout will exit the user from login.

    Tasks
    * Install django-allauth
    * Create the template
    * Test Functionality

  ### USER STORY: Bag Items 16
 
    As a shopper I want to be able to view a list of products in my bag before making payment so that I can see the items and total cost and quantity

    Acceptance Criteria
    Given the user has to know how much the total is When they view the basket. Then happens product subtotal is visible along with the delivery charge and grand total

    Tasks
    * Add totals to checkout view
    * Add html to template

  ### USER STORY: Add 17
    
    As a store owner I want to be able to add a new product to the store so that I can offer customers the latest products

    Acceptance Criteria
    When the store owner adds a product. Then this becomes available on the site for customers to purchase

    Tasks
    * Create add product view
    * Create product form
    * connect URL's
    * Add decorator to protect view

  ### USER STORY: Delete 18
    
    As a store owner I want to be able to delete products so that I can remove products that are out of stock or discontinued

    Acceptance Criteria
    Given a store owner will want to delete a product that is out of stock. When they delete a product. Then this product is no longer available on the site for customers to purchase

    Tasks
    * Create delete product view
    * connect URL's
    * Add decorator to protect view

  ### USER STORY: Edit 19

    As a store owner I want to be able to edit products on the website so that I can make changes to the product details e.g., price if products on sale

    Acceptance Criteria
    Given that a store owner may want to edit a products price or information. When the store owner edits a product. Then this change is updated on the products page of the website.

    Tasks
    - Create update product view
    - Use product form
    - connect URL's
    - Add decorator to protect view &nbsp;


  ### USER STORY: Product details 20

    As a shopper I want to be able to view the products details so that I can read the product description

    Acceptance Criteria
    Given that the user can view more information on each product. When they click on a product, then they are directed to the product details page

    Tasks
    * Create product detail view,
    * Create product detail template and style.
    * Connect URL's.

## Bugs
 
  * One of the bugs that I encountered when creating the website was was in basket on mobile devices. The right side of the screen would push everything including the footer to the right. This resulted in a white line down the right of the screen. The text was slightly moved to the right also. I spent a long time trying to fix the issue. When I loaded the deployed site on my phone and went to the basket the page looked fine and didnt have this same issue. I eventually contacted tutuor support and they tried to help but we couldnt fix it. The tutor Alex tried the website on firefox and some other browsers and the basket worked fine. 

  * On the product details page the images when clicked on download the file. I was trying to get the image to open up on a new tab. I changed the image  I tried removing the link but was unable to fix this one.

 # Marketing<div id='marketing'>

## Social Media
As part of the project we had to use a marketing campaign to promote our ecommerce website. I created a facebook page for the business. Facebook is a great marketing tool as it allows the shop owner to connect with customers and its a great way grow a business. With Facebook's global reach, this will help gain more customers. The companies website is on the Facebook page as this will increase traffic and to attract potential customers.

![facebook marketing](https://user-images.githubusercontent.com/91072896/193131616-cc01c9a9-4450-46f8-8381-0c08af95b8d2.png)
 
## SEO
 I created a robots.txt to allow it to be ranked higher and sitemap.xml file to allow for faster search results this will improve the quality and quantity of website traffic. I used wordtracker to see if what key words gain the most traffic and to get an idea what I can use in my website. I searched playstation xbox and nintendo the results are shown below. This along with looking at other similar websites help me come up with these keywords.
![Screenshot 2022-09-29 23 22 27](https://user-images.githubusercontent.com/91072896/193154113-27445438-72a7-40e4-a1d0-e9acf82a3ecf.png)
![Screenshot 2022-09-29 23 22 02](https://user-images.githubusercontent.com/91072896/193154217-e9f4ad20-8df9-4165-a9ed-a62c3ce6edf6.png)

![Screenshot 2022-09-29 23 34 58](https://user-images.githubusercontent.com/91072896/193154140-8737fd3b-610f-4c68-8442-f7122ca28fe2.png)

## Keywords
The meta tags and descriptions have relevant information and keywords that are picked up in a google search  Beow are a list of the key words used in my websites meta tags and descriptions.
![Screenshot 2022-09-29 23 49 04](https://user-images.githubusercontent.com/91072896/193155623-973d033e-7324-4c8a-be65-d52ce25f50da.png)

## Newsletter
 When a customer visits our site they can sign up to our newletter. The is located in the footer of our website. The user can enter there email address an they will then receive updates about sales and othe information.