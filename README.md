# relationship-quarrel

![amiresponsive]()

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

Target Audience:

- 18-40 year olds
- People who are looking to take arguments with a bit of comedy
- People who would like to improve their communication skills
- People who've seen too many one-sided-stories

The audience is looking for something where both sides are visible. With the ability to post both arguments and hash it out once and for all, with complete strangers on the internet, the site allows the user to read different points of views and thereafter see whose argument was the best.

## Design/Structure


Apps:



### Databases:

Quarrelapp holds all the databases, consisting of:

1. Post in combination with CommentPost allows for the ability of letting the user create a post, but through a OneToOneField with CommentPost, separate the likes and comments. Through the ability of calling different keys, connected to each argument, it allows for the possibility of cross-liking as well as future customization of the comment section(more on that in improvements) With each post, the model generates the users post but splits the content one and content two into separate keys which are then callable in views.
2. Comment allows for users to comment on posts with date-stamps, as well as Post, have a built-in CASCADE in order to delete all comments related to user if user decided to delete their account.

Below is a diagram of the correlation between the models:

![database-schema]()

### Planning

I wireframed it using Balsamiq:

Landing page:

![wireframe]()

Landing page - Mobile:

![wireframe]()

A post full screen:

![wireframe]()

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
