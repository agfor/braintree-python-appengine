#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

try:
    # This is needed to make local development work with SSL.
    # This must be done *before* you import the Braintree Python library.
    # See http://stackoverflow.com/a/24066819/500584
    # and https://code.google.com/p/googleappengine/issues/detail?id=9246 for more information.
    from google.appengine.tools.devappserver2.python import sandbox
    sandbox._WHITE_LIST_C_MODULES += ['_ssl', '_socket']

    import sys
    # this is socket.py copied from a standard python install
    import stdlib_socket
    sys.modules['socket'] = stdlib_socket
except ImportError as e:
    print(e)

import webapp2
import braintree

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    'use_your_merchant_id',
    'use_your_public_key',
    'use_your_private_key'
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        result = braintree.Transaction.sale({
            "amount": "10.00",
            "credit_card": {
                "number": "4111111111111111",
                "expiration_date": "05/2020"
            }
        })
        self.response.write("Look at this page with view source.\n")
        if hasattr(result, 'message'):
            self.response.write(result.message + "\n")
        if hasattr(result, 'transaction'):
            self.response.write(result.transaction.status + "\n")
            self.response.write(repr(result.transaction))
        if hasattr(result, 'errors') and result.errors.deep_errors:
            self.response.write(repr(result.errors.deep_errors))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
