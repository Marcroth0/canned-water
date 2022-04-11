# canned-water

![amiresponsive]()

Welcome to Dropp. Website! Dropp is an ecommerce platform, equipped with authentication (user-accounts) that not only sells its brand but also sells their products and merchandise. All using HTML, CSS(bootstrap), Javascript(jQuery), Python, Django, and deployment to Heroku with AWS holding the reigns of static files. Not to mention Stripe, the payment system integrated.

Live link: https://quarrel2022.herokuapp.com/

## About:

### Table of Contents

1. [User Stories](#user-stories)
2. [UX](#ux)
   1. [Strategy](#strategy)
   2. [Design/Structure](#design/structure)
   3. [Databases](#databases)
   4. [Planning](#planning)
   5. [End Design](#end-design-result)
3. [Testing](#testing)
   1. [Manual Testing](#manual-testing)
   2. [Validator](#validator-testing)
   3. [Bugs](#unfixed-bugs)
   4. [Improvements](#improvements)
4. [Credits](#credits)

### User Stories

View my User Stories and planning [here](https://github.com/Marcroth0/relationship-quarrel/issues).

# UX

## Strategy

The initial and primary goal of the website is to create an e-commerce platform that looks great. This is not 100% dedicated to ecommerce, but to the brand itself. Sell the brand, sell the product. It allows a user to easily navigate the site and interact with the products via reviews, as well as the owners via the contact form.

Target Audience:

- 18-40 year olds
- People who are tired of plastic
- People who are environmentally friendly

The visitors are looking for a product that makes caring about the environment cool.

## Design/Structure

Apps and their core functionality:

- Checkout
  Handle successful checkouts and saves order to userprofile,
  Validating checkout process,
  Caches the cart and user data, returns error of unvalid

- Connect
  View to let users send email to owner of site

- Home
  A view to show individual product details through ajax
  A view for index

- Products
  A view to show all products, including sorting and search queries
  A view to show individual product details
  Add/delete user reviews
  add/edit/delete products

- Profiles
  Get and view userprofile including: Get and view order history
  Edit/add/delete Wishlist items.

- Bag
  A view that renders the bag page
  Add a quantity of the specified product to the shopping bag
  Adjust the quantity of the specified product to the shopping bag
  Delete the item from the shopping bag

- Articles
  Add, edit, and delete Articles/blogs

### Databases:

### Models:

- Articles, Models Post:
  title: Stores title of article
  author: Stores the author(ForeignKey) taken from User
  description = Stores the description of the Blog tied to user
  image: Imagefield
  body: The content
  date_published: Automatic date_published field
  featured_articles: Boolean field, if true = featured.

- Bag, Models Order/OrderlineItem:
  Stores all information about the order. The user information, such as address, email, phone number, address etcetera - order information including price + delivery, products and quantity, and a stripe_pid intent ID - ties all information to the user_profile.

- Connect Models:
  email Stores information about used email
  title: Subject of email
  content: Content of email

- Profile:
  A user profile model for maintaining default
  delivery information(address, email, phone-number, etcetera) and order history

- Review:
  product: Stores the product with the related name of 'reviews', connected to user - both in foreignkeys.
  content: Stores content of review
  stars: stores the rate
  date_published: Stores when the review was published

Below is a diagram of the correlation between the models:

![database-schema]()

### Planning

I wireframed it using Balsamiq:

Landing page:
![wireframe](readme-files/readme/balsamiq-landing-readme.png)

Structure:
![wireframe](readme-files/readme/balsamiq-overall-readme.png)

Products Page:
![wireframe](readme-files/readme/balsamiq-products-readme.png)

I had the initial idea in my head to make it visually appealing, considering the goal was to make an ecommerce for the Company with few products where the brand was in focus. The breadcrumbs througout the page, going from products/bag/checkout, and wishlist/profile/order history.

### End Design Result:

Easily navigated navbar containing a home button, disguised as a logo, an about-page, a registration and a login-button that catches the visitors eye.

Navbar:
![navbar]()

For users that are logged in, the post-button swaps to an account button, containing: My posts, deactivate account, delete account, as well as logout. The register button is replaced with an additional post-button.

Navbar(Logged in):
![navbar]()

Landing page is a cooperation between the hero-image and the Quarrels-section. Instantly the visitor gets questions answered:

1. What the point of the site is
2. The possibility of being a part of it
3. How the posts are portrayed on the landing page

These three points together form a need to be included.

Hero:
![hero]()

Quarrels:
![quarrels]()

Post Detail:
![postdetail]()

About page:
![about]()

Footer:
![footer]()

Whimsical writings:

### Color Palette

Colors:
![palette]()

### Reasoning

The design of the website was crucial. It being a "argument-solver" it needed to be peculiar and not take the initial argument, or the definition of an argument, all that seriously. With the ability of seeing it, instead of an obstacle, as a "funny challenge" to post it to the internet. Hence the sarcastic comments spread around the website. With a comical twist, on serious subjects, it will hopefully invoke a funny tone in the comments as well as an appearance of the "good side" of the internet which are there to actually help, inbetween a sea of funny anti-comments. (Comments mainly meant to ridicule)

### Fonts

Font-family: "Mochiy Pop P One", Montserrat;

##

## CRUD

- The user has the ability to
  C - reate their own post.
  R - read their, or others posts and comments.
  U - update their post
  D - delete their post and comments, as well as their account.

## Testing

I tested the responsiveness of the site on the below units, using chrome dev as well as some in real life testing:

**Mobile**

- Moto G4 (360x640)
- Galaxy S5 (360x640)
- Pixel 2 (411x731)
- Pixel 2 XL (411x823)
- iPhone 5/SE (320x568)
- iPhone 6/7/8 (375x667)
- iPhone 6/7/8 Plus (414x736)
- iPhone X (375x812)
- iPad (768x1024)
- iPad Pro (1024x1366)

**Browsers:**

- Chrome
- Mozilla Firefox
- Safari

### Manual testing

See further on click [here]()

### Lighthouse

![lighthouse]()

### Validator Testing

W3 HTML Validator:

![html]()

W3 CSS Validator:

![css]()

For Python I've used pep8 validator which resulted in 0 errors on all pages.

## Unfixed Bugs

1. There's a bug where if you type one very, very long word, without spaces, in argument one or two, the post_details overflows.
2. CommentPost (content one and two) aren't successfully deleted from DB. Have to add functionality in already existing delete-function to also include this.

## Technologies used:

- I used [Python](https://www.python.org/) to write my functions and models

- [Django](https://www.djangoproject.com/) is the framework used to build project and its apps

- [Cloudinary](https://cloudinary.com/) has been used to store my images and static files

- [Crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/) has been used to easily display forms

- [Github](https://github.com/) Has been to store and plan project

- [Vscode](https://code.visualstudio.com/) my choice of IDE

- [PostgreSQL](https://www.postgresql.org/) Database

- [SQlite](https://www.sqlite.org/index.html) has been used for local testing

- [Pep8](https://pypi.org/project/autopep8/) has been used for formatting and error-checking python-code

- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) has been used for formatting and error-checking html-code

- [ImgBot](https://imgbot.net/) - my trustworthy companion for optimizing size of images

- [Google-Developer-Tools](https://developers.google.com/web/tools) - for debugging

- [Bootstrap4](https://getbootstrap.com/) - css library

- [AmIResponsive](http://ami.responsivedesign.is/#) - used to check responsiveness, and collect image you find at the top of page.

## Features Left to Implement

## Deployment

The site was deployed using Heroku, following the steps offered by Codeinstitute. Instructions are found [here](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

Heroku:

AWS - static:

## Credits

- A general shout-out to [StackOverflow](https://stackoverflow.com/), which solved a lot of issues.
- Credit for images used in posts [chikenbugagashenka](https://www.freepik.com/free-vector/boys-girls-kids-aggression-conflict-set_20892288.htm#query=argue&position=11&from_view=search)
- [dbdiagram](https://dbdiagram.io/) for offering a database-visualiser
