def filter_by_country(data, country):
  country_data = list(filter(lambda item: item['Country'] == country, data))
  return country_data


def delete_columns(country_data):
  new_country_data = dict(
    filter(
      lambda item: 'Population' in item[0] and 'Percentage' not in item[0],
      country_data[0].items()))
  return new_country_data


def format_key(data):
  new_data = data.copy()
  new_data = {k[0:4]: v for k, v in new_data.items()}
  return new_data


def get_population(country_data):
  population_data = delete_columns(country_data)
  population_data = format_key(population_data)
  return population_data.keys(), population_data.values()

