from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)


max_results = die_1.sides * die_2.sides + die_3.sides
frequencies = [results.count(value) for value in range(3, max_results+1)]


x_values = list(range(3, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title='Results of Rolling three D6 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3_d6.html')
