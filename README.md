# Amazing_Books
Created a book review website named Amazing books using **python, flask, SQLAlchemy, HTML, CSS and Bootstrap**.

---
In this project, I built a book review website. Users will be able to register for the website and then log in using their username and password. Once they log in, they will be able to search for books, leave reviews for individual books, and see the reviews made by other people. I also used the a **third-party API by Goodreads**, another book review website, to pull in ratings from a broader audience. Finally, users will be able to query for book details and book reviews programmatically via the website’s API.


---
**create.sql** file - 3 tables were used in my database namely users, books and reviews. The file includes SQL commands to create those 3 tables with relevant relationships.

---

**import.py file** -  this file reads books.csv and imports books into the database 

---

**5 html pages** were used and they are located in templates folder. 

---

**layout.html** - This is the template containing HTML skeleton, the navigation bar, the header and the footer.  All other 4 html pages in this app are inherited  from this file.   

---

**index.html** - landing page of the website. if user already has’t got an account, then the user can sign-up providing a username and password.  Having created an account, the user can sign-in with the username and password. Passwords are saved to the data base using python md5 hash. I have added some server side validation for sign in and sign up functions. Since still we haven’t learnt about javascript yet, there is no client side validation to expect a default message for all input fields with required attribute.

Server side validation for sign-up function
1. Verify whether user has entered username, password and confirm password fields
2. Verify whether the password field is correct and confirm password field match
3. Verify whether the username is available (whether not already taken)

Server side validation  for sign-in
1. Verify whether user has entered the  username and password fields
2. Verify whether username and password is a valid match

---

**welcome.html** - this will be the home page of the website once a user has logged in. The page mainly has a search panel where user can search for books using the title, author or ISBN. If a user performed a search, then matching results are displayed on the same page. If there are no matching results, a message will be displayed on the same page. 

---

**book.html**   - When users click on a book from the results of the above page, they will be directed to this page, with details about the book:Such as its title, author publication year, ISBN number, and any reviews that other users have left regarding the book on this website. Also the average rating and number of ratings the work has received from the Goodreads which a third party API. In addition users are able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component. If users try to submit multiple reviews for the same book, then there is an error message notifying “You have already added a review for this book”.

---

**error.page** - If there are any unexpected searches, users will observe this page with an error message.

---

**API Access** - website url/api/<isbn> - (where <isbn> is an ISBN number), this is a JSON response containing the book’s title, author, publication date, ISBN number, review count, and the average score. If the requested ISBN number isn’t in the database, it returns a 404 status error with the message “ISBN not found”

---

**requirements.txt** - contains Python packages that need to be installed in order to run the web application, apart from the packages which were already mentioned in projects startup package, I had to install “requests” package.

---

**application.py** file - Flask code is stored inside this file. 9 routes were used.
1. route(“/") - for displaying the index page
2. route("/register", methods=[“POST"]) - sign-up a new user
3. route("/login", methods=[“POST"]) - sign - in a user
4. route(“/logout") - sign out a user who is logged to the system
5. route(“/home") - render welcome.html with book search panel
6. route("/search", methods=[“POST"]) - performed the search and display search 			results on welcome.html
7. route(“/books/<int:book_id>") - to see more details about a selected book
8. route("/review", methods=[“POST"]) - adding a review
9. route(“/api/<isbn>") - API access which returns JSON

---

**styles.css**  - main css file which is located in static folder

---

**RAW SQL commands** (as via SQLAlchemy’s execute method) were used in order to make database queries

---
Note: All pages are responsive, Bootstrap components were used

---

[Link to screencast](https://www.youtube.com/watch?v=31iCJzzbng4) or View web app on action https://www.youtube.com/watch?v=31iCJzzbng4

