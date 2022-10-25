import charts
import utils
import read_csv


def run():
  data = read_csv.read_csv('data.csv')
  country = input("Escriba el país: ")
  #country = "Colombia"
  country_data = utils.filter_by_country(data, country)
  labels, values = utils.get_population(country_data)
  charts.generate_bar_chart(country, labels, values)


if __name__ == '__main__':
  run()
