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
    <li><a href="#video-demo">Video Demo</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![homepage](/demo/homepage.png)

**Hubinance**, short for "Hubie Finance", is a stock-trading web app with portfolio management functionality. Leveraging IEX's API, users are able to check the real time value of their portfolio and obtain price quotes for individual stocks. Users will also be able to buy and sell stocks via market order and track their transaction history.

View source code [here](/app.py).

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Bootstrap 5](https://getbootstrap.com)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- VIDEO DEMO -->
## Video Demo
Timestamps:
* 00:03 - Registering new user and logging in
* 00:36 - Changing cash balance via back-end *(customizability for initial cash balance not available)*
* 00:52 - Buying stocks from Dashboard
* 01:00 - Selling holdings from Dashboard
* 01:13 - Viewing transaction history
* 01:19 - Obtaining price quote for ticker and buying quoted ticker
* 01:52 - Error handling for buying invalid ticker
* 02:02 - Error handling for selling quantity > available holdings

https://user-images.githubusercontent.com/86993236/151592003-8ae86b59-b4f8-4d17-bdb3-74d74c3b1be1.mp4

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps below (Windows):

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

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [CS50](https://cs50.harvard.edu/x/2022/psets/9/finance/)
* [IEX](https://iexcloud.io/cloud-login#/register/)

<p align="right">(<a href="#top">back to top</a>)</p>
