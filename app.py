import web, json

render = web.template.render('templates/')
urls = (
    '/moving\-averages', 'display_html',
    '/moving\-averages/json', 'display_json',
    '/data/(.*)', 'data'
)

averages = {
    'numbers': [],
    'simple': 0.0,
    'cumulative': 0.0,
    'weighted': 0.0,
    'exponential': 0.0,
}

class data:
    def POST(self, num):
        try:
            num = float(num)
            averages['numbers'].append(num)
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

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
