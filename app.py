import web, json, random, average_calculations
from datetime import *

render = web.template.render('templates/')
urls = (
    '/data/(.*)', 'data',
    '/moving\-averages', 'display_html',
    '/moving\-averages/json', 'display_json',
    '/generate-data/(\d+)', 'generate_data',
)

averages = {
    'numbers': [],
    # Configure this to be the period for average calculations
    'period': timedelta(seconds=10),
    'simple': 0.0,
    'cumulative': 0.0,
    'weighted': 0.0,
    'exponential': 0.0,
}

def update_averages(num):
    period = averages['period'].seconds

    time_now = datetime.now()
    averages['numbers'].append({'number': num, 'time': time_now})
    len_nums = len(averages['numbers'])

    # Simple Moving Average
    sma_list = averages['numbers'][len_nums-period:]
    averages['simple'] = sum(map(lambda x: x['number'], sma_list))/len(sma_list)

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
        for i in range(0, (n if n <= 50 else 50)):
            update_averages(random.uniform(7.0, 10.0))
        return web.seeother("/moving-averages")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
