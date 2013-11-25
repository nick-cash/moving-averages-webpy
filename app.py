import web

urls = (
    '/', 'moving_averages'
)

class moving_averages:
    def GET(self):
        return "Success."

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()