import web, json, random
from datetime import *
from moving_averages import *

render = web.template.render('templates/')
urls = (
    '/data/(.*)', 'data',
    '/moving\-averages', 'display_html',
    '/moving\-averages/json', 'display_json',
    '/generate-data/(\d+)', 'generate_data',
)

averages = {
    'numbers': [],
    # Configure this to be the period for average calculations.
    'period': 10,
    'simple': [],
    'cumulative': [],
    'weighted': [],
    'exponential': [],
}

def update_averages(num):
    averages['numbers'].append(num)

    period = averages['period']
    len_nums = len(averages['numbers'])

    # Simple Moving Average
    averages['simple'].append(simple_moving_average(averages['numbers'], period))

    # Cumulative Moving Average
    if len_nums > 1:
        averages['cumulative'].append(cumulative_moving_average(averages['numbers'],
                                                                averages['cumulative'][-1]))
    else:
        averages['cumulative'].append(num)

    # Weighted Moving Average
    averages['weighted'].append(weighted_moving_average(averages['numbers'], period))

    # Exponential Moving Average
    if len_nums > 1:
        averages['exponential'].append(exponential_moving_average(averages['numbers'],
                                                                  period,
                                                                  averages['exponential'][-1]))
    else:
        averages['exponential'].append(num)

# Page handlers
class data:
    def POST(self, num):
        try:
            num = float(num)
            update_averages(num)
            ret_val = 'success'
        except ValueError:
            ret_val = 'failure'
            num = "not a number"
        web.header('Content-Type', 'application/json')
        return json.dumps({ret_val: num})

class display_html:
    def GET(self):
        return render.moving_averages(averages)

class display_json:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(averages)

class generate_data:
    def GET(self, number_of_datapoints):
        n = int(number_of_datapoints)
        for i in xrange(0, (n if n <= 50 else 50)):
            update_averages(random.uniform(1.0, 20.0))
        return web.seeother("/moving-averages")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
