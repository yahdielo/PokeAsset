# Python Data Scrapper

The python_webscraper is a tool designed to scrape sales data for specific cards from eBay. It utilizes the BeautifulSoup library to extract the necessary information. Once the data is retrieved, the tool performs several cleaning operations. It removes unwanted objects based on non-matching titles, cleans and formats the sold dates into Datetime format, and converts the sold prices into integers for easier manipulation and analysis.

Once we have obtained the desired clean data, we save it into a JSON file for storage and future reference. This JSON file serves as the data source for generating a chart in the index.html file. We use the Chart.js library to create the chart, which visually maps all the card sales based on the collected data. This chart provides a graphical representation of the sales trends and patterns for the cards.

## Tools

Web Scrapping: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Data Manipulation: [Numpy](https://numpy.org/) & [Pandas](https://pandas.pydata.org/)
Data visualizatio: [Chart.js](https://www.chartjs.org/docs/latest/)
Data:
- [PokeAPI](https://pokeapi.co/)
- [Pokedex](https://pokemondb.net/pokedex/all)
- [Dataset](https://www.kaggle.com/datasets/05bffa9809b39a7ddc851d80104b1fa314e4ef36700ce74a2c91d8b3c8113112)
- [Dataset2](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9monurmi_by_National_Pok%C3%A9dex_number)

## Requirements

## How to use it?

To run in, install  beautifulSoup, assumming you already have python and pip.

Clone the repo to your computer:

    git clone //repo url//

Move inside the repo and then, type in terminal:

    python3 ./name_of_file

## Example of the data display

![CHarizard v max rainbow rare Historic prices](./imgs/home_page.png)
![CHarizard v max rainbow rare Historic prices](./imgs/stats_page.png)

