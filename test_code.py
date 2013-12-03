import json
from nose.tools import *
from unittest import TestCase
from app import *

class TestCode(TestCase):
    def setUp(self):
        self.app = web.application(urls, globals())
        init_averages()

    def test_index(self):
        r = self.app.request('/')
        assert_equal(r.status, "200 OK")

    def test_405s(self):
        r = self.app.request('/data/10', method='GET')
        assert_equal(r.status, "405 Method Not Allowed")

        r = self.app.request('/', method='POST')
        assert_equal(r.status, "405 Method Not Allowed")

        r = self.app.request('/moving-averages', method='POST')
        assert_equal(r.status, "405 Method Not Allowed")

        r = self.app.request('/moving-averages/', method='POST')
        assert_equal(r.status, "405 Method Not Allowed")

        r = self.app.request('/moving-averages/json', method='POST')
        assert_equal(r.status, "405 Method Not Allowed")

        r = self.app.request('/generate-data/10', method='POST')
        assert_equal(r.status, "405 Method Not Allowed")

    def test_bad_urls(self):
        r = self.app.request('/data', method='POST')
        assert_equal(r.status, "404 Not Found")

        r = self.app.request('/moving_averages')
        assert_equal(r.status, "404 Not Found")

        r = self.app.request('/moving-averages/json/')
        assert_equal(r.status, "404 Not Found")

        r = self.app.request('/moving_averages/json')
        assert_equal(r.status, "404 Not Found")

    def test_data_bad_number(self):
        r = self.app.request('/data/notanumber', method='POST')
        assert_equal(r.status, "200 OK")
        assert_equal(r.headers, {'Content-Type': 'application/json'})
        assert_equal(r.data, json.dumps({'failure': 'not a number'}))

    def test_data_no_number(self):
        r = self.app.request('/data/', method='POST')
        assert_equal(r.status, "200 OK")
        assert_equal(r.headers, {'Content-Type': 'application/json'})
        assert_equal(r.data, json.dumps({'failure': 'not a number'}))

    def test_data_numbers(self):
        r1 = self.app.request('/data/99999.999999', method='POST')
        assert_equal(r1.status, "200 OK")
        assert_equal(r1.headers, {'Content-Type': 'application/json'})
        assert_equal(r1.data, json.dumps({'success': 99999.999999}))

        r2 = self.app.request('/data/10', method='POST')
        assert_equal(r2.status, "200 OK")
        assert_equal(r2.headers, {'Content-Type': 'application/json'})
        assert_equal(r2.data, json.dumps({'success': 10.0}))

        r3 = self.app.request('/moving-averages/json')
        assert_equal(r3.status, "200 OK")
        assert_equal(r3.headers, {'Content-Type': 'application/json'})
        data = json.loads(r3.data)
        assert_equal(data[0][0][1], 99999.999999)
        assert_equal(data[0][1][1], 10.0)

    def test_display_json_blank(self):
        r = self.app.request('/moving-averages/json')
        assert_equal(r.status, "200 OK")
        assert_equal(r.headers, {'Content-Type': 'application/json'})
        assert_equal(r.data, json.dumps([[],[],[],[],[]]))
