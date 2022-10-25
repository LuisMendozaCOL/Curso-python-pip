import charts
import utils
import read_csv
import pandas as pd


def run():
  country = input("Escriba el país: ")
  
  df = pd.read_csv('data.csv')
  region = 'South America'
  df = df[df['Continent'] == region]
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart('region', countries, percentages)
  
  data = read_csv.read_csv('data.csv')
  country_data = utils.filter_by_country(data, country)
  labels, values = utils.get_population(country_data)
  charts.generate_bar_chart(country, labels, values)
  
  



if __name__ == '__main__':
  run()
