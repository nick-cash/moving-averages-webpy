import web, json, random
from datetime import *
from moving_averages import *

render = web.template.render('templates/')
urls = (
    '/data/(.*)', 'data',
    '/moving\-averages', 'display_html',
    '/moving\-averages/', 'redirect',
    '/moving\-averages/json', 'display_json',
    '/generate-data/(\d+)', 'generate_data',
)

# Configure this to be the period for average calculations.
PERIOD = 10

averages = {
    'numbers': [],
    'simple': [],
    'cumulative': [],
    'weighted': [],
    'exponential': [],
}

def update_averages(num):
    averages['numbers'].append(num)

    len_nums = len(averages['numbers'])

    # Simple Moving Average
    averages['simple'].append(simple_moving_average(averages['numbers'], PERIOD))

    # Cumulative Moving Average
    if len_nums > 1:
        averages['cumulative'].append(cumulative_moving_average(averages['numbers'],
                                                                averages['cumulative'][-1]))
    else:
        averages['cumulative'].append(num)

    # Weighted Moving Average
    averages['weighted'].append(weighted_moving_average(averages['numbers'], PERIOD))

    # Exponential Moving Average
    if len_nums > 1:
        averages['exponential'].append(exponential_moving_average(averages['numbers'],
                                                                  PERIOD,
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

# Redirect on slash, we are going slashless
class redirect:
    def GET(self):
        raise web.seeother("/moving-averages")

class display_json:
    def GET(self):
        web.header('Content-Type', 'application/json')
        def format_jqplot(key):
            lst = []
            for i,num in enumerate(averages[key]):
                lst.append([i,num])
            return lst
        formatted = []
        formatted.append(format_jqplot('numbers'))
        formatted.append(format_jqplot('simple'))
        formatted.append(format_jqplot('cumulative'))
        formatted.append(format_jqplot('weighted'))
        formatted.append(format_jqplot('exponential'))
        return json.dumps(formatted)

class generate_data:
    def GET(self, number_of_datapoints):
        n = int(number_of_datapoints)
        for i in xrange(0, (n if n <= 50 else 50)):
            update_averages(random.uniform(1.0, 20.0))
        return web.seeother("/moving-averages")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
