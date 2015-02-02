braintree-python-appengine
==========================

See it running at http://braintree-python.appspot.com/

The main points here are:
1. Have billing enabled for the google app engine account.
2. See the [comment in main.py](https://github.com/agfor/braintree-python-appengine/blob/master/main.py#L28-L40) for how to get SSL working in development mode.
3. Add `ssl` to your [app.yaml](https://github.com/agfor/braintree-python-appengine/blob/master/app.yaml#L18-L19).
4. If you still have problems, make sure you have a recent version of Requests installed.
