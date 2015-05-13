braintree-python-appengine
==========================

See it running at http://braintree-python.appspot.com/

The main points here are:

1. Have billing enabled for the google app engine account.
2. See the `try` block in main.py for how to get SSL working in development mode.
3. Add `ssl` to your [app.yaml](https://github.com/agfor/braintree-python-appengine/blob/master/app.yaml#L18-L19).
4. Use a working version of requests, or set the GAE_USE_SOCKETS_HTTPLIB environmental variable in your app.yaml.

requests versions 2.6.1, 2.6.2, and 2.7.0 use versions of urllib3
that don't work correctly with the App Engine urlfetch API.
Either use a different version of requests or [see this github issue for a workaround](https://github.com/kennethreitz/requests/issues/2595).
