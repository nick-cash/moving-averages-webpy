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

----------------
- Instructions -
----------------
1. Setup
    - Install Python 2.7
    - Install web.py
        -> sudo pip install web.py

2. Configure
    - Change PERIOD in app.py to any time period you desire. This will change
      how all of the averages are calculated.

3. Run
    -> python app.py

4. Input or generate some data
    -> POST /data/{x} where {x} is a valid float
        * Use this to input a single number you specify
        * Response is a json object with a success or failure message

    -> GET /generate-data/{x} where x is an integer between 1 and 50
        * Use this to generate 1 to 50 random floats between 1.0 and 20.0
        * Redirects to /moving-averages

5. View data
    -> /moving-averages
        * Displays a graph with all of our data and the following moving averages:
            - Simple Moving Averages
            - Cumulative Moving Averages
            - Weighted Moving Averages
            - Exponential Moving Averages

          You can click and drag to zoom in on particular data. Double click to reset
          the zoom. You can also toggle the various series on and off by clicking it
          in the legend. The graph will update every 60 seconds if new data is present.

    -> /moving-averages/json
        * Returns a json object that contains all of the data currently held in
          memory by the application. It is formatted to be used by jqPlot, but could
          easily be used for other things. If you wish to access the data, the lists
          are always generated in the following order:
            - Data
            - Simple Moving Averages
            - Cumulative Moving Averages
            - Weighted Moving Averages
            - Exponential Moving Averages

-----------
- License -
-----------
Written by Nick Cash, November 2013.

This code is public domain. Use it as you wish.
