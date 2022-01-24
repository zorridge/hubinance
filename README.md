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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

**Hubinance**, short for "Hubie Finance", is a web app where you can manage a portfolio of stocks. Leveraging IEX's API, the user is able to check for stocks' real time values and their own portfolio's value. The user will also be able to buy and sell stocks and track their transaction history.

Part of Harvard's CS50 (Problem Set 9), this is my own unique solution on the problem where I have implemented additional unique features using the knowledge I have acquired from the course. `helpers.py` is written by the CS50 staff, as well as the initial Flask app set up in `app.py`, everything else is written and styled by me. 

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python 3](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Bootstrap 5](https://getbootstrap.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps below (Windows):

### Prerequisites

Ensure that the latest version of Python 3 is installed (writtin in Python 3.10.1)
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

Todo

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Implement responsive design for desktop
- [ ] Implement responsive design for mobile
- [ ] Add "Quote" function to Dashboard

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [CS50](https://cs50.harvard.edu/x/2022/psets/9/finance/)
* [README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>
