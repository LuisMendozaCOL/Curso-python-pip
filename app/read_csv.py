import csv


def read_csv(path):
  with open(path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    #print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #print('***' * 5)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      #print(country_dict)
      data.append(country_dict)
    return data


if __name__ == '__main__':
  pass
  #data = read_csv('./App/data.csv')
  #print(data[0])
