# Hubie Finance

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![homepage](/demo/homepage.png)

**Hubinance**, short for "Hubie Finance", is a web app where you can manage a portfolio of stocks. Leveraging IEX's API, users are able to check for an individual stock's and their portfolio's real time value. Users will also be able to buy and sell stocks and track their transaction history.

Part of Harvard's CS50 module (Problem Set 9), this is my solution to the problem where I have also additionally implemented unique features using the knowledge I have acquired from the course and beyond. `helpers.py` is written wholly by the CS50 staff, as well as the initial Flask app set up in `app.py`. Everything else is written and styled by me. 

### Built With

* [Python 3](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Bootstrap 5](https://getbootstrap.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps below (Windows):

### Prerequisites

Ensure that the latest version of Python 3 is installed (written in Python 3.10.1)
* python
  ```sh
  python --version
  ```

### Installation

1. Get a free API Key at [https://iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/)
2. Clone the repo
   ```sh
   git clone https://github.com/zorridge/hubinance.git
   ```
3. Install required modules
   ```sh
   pip install Flask
   pip install Flask-Session
   pip install cs50
   ```
4. Enter your API in the terminal
   ```sh
   set API_KEY='ENTER YOUR API'
   ```
5. Run Flask
   ```sh
   flask run
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
* Registering/logging-in via the landing page *(user data is managed by a SQLite database and the password is hashed using the `werkzeug.security.generate_password_hash()` function)*

![register](/demo/register.png)

* Arriving at the homepage *(initial cash balance will always default to $10,000 for new users)*

![new user homepage](/demo/homepageEmpty.png)

* Obtaining a price quote for a ticker

![quote](/demo/quote.png)

* Placing a market order for the quoted ticker

![quoted](/demo/quoted.png)

* Viewing the transaction history

![history](/demo/history.png)

### Live Demo
Coming soon...

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Implement responsive design for desktop
- [ ] Implement responsive design for mobile
- [ ] Film live demo of web app
- [ ] Add "Quote" function to Dashboard

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [CS50](https://cs50.harvard.edu/x/2022/psets/9/finance/)
* [README.md Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>
