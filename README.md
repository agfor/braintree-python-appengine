braintree-python-appengine
==========================

See it running at http://braintree-python.appspot.com/

The main points here are:

1. Have billing enabled for the google app engine account.
2. See the `try` block in main.py for how to get SSL working in development mode.
3. Add `ssl` to your [app.yaml](https://github.com/agfor/braintree-python-appengine/blob/master/app.yaml#L18-L19).
4. Use a working version of requests, or set the `GAE_USE_SOCKETS_HTTPLIB` environmental variable in your app.yaml.

requests versions 2.6.1, 2.6.2, and 2.7.0 use versions of urllib3
that don't work correctly with the App Engine urlfetch API.
Either use an earlier version of requests or [use this commit from my branch of requests to fix it](https://github.com/agfor/requests/commit/655dc083bb020a30ddf9c2c6202bbc0c8b39cb58). [See this github issue for more information](https://github.com/kennethreitz/requests/issues/2595).

Starting with requests 2.10.0, it should be possible to use requests-toolbelt's AppEngineAdapter instead of the fix listed above. See the [requests-toolbelt docs for more information](https://github.com/sigmavirus24/requests-toolbelt/blob/master/docs/adapters.rst#appengineadapter).
