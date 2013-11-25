-----------------
- Specification -
-----------------

Build a simple web service that computes moving averages. Data will be sent to the web service via an HTTP request:

POST /data/{x}

Where {x} is any number like 1 or 2.34.

The system should calculate simple, cumulative, weighted and exponential moving averages. The current value of each moving average should be available via a GET request, like:

GET /moving-averages

The HTTP response should contain current values for simple, cumulative, weighted and exponential moving averages. It could be a simple JSON object or may be an HTML page for viewing in a browser. If you want to get really creative, you could provide an HTML page which gets new moving average values pushed to it after new data arrives.

There is no need to maintain data in a persistent data store; keeping values in-memory is fine. Put the project in a repo with a brief README.

---------
- Setup -
---------

- Install Python 2.7
- Install web.py
 -> sudo pip install web.py

-----------
- License -
-----------

Written by Nick Cash, November 2013.

This code is public domain. Use it as you wish.
