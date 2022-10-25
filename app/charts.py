import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  #plt.show()
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  #plt.show()
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

if __name__ == '__main__':
  pass
  #labels = ['a','b','c']
  #values = [10,200,300]
  #generate_bar_chart(labels, values)
  #generate_pie_chart(labels, values)
