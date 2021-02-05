.. _refresh_token:

Working with Refresh Tokens
===========================

TODO: this page needs to be updated to provide an example of how to use the obtained
refresh_token.

The following program can be used to obtain a refresh token with the desired scopes.
Such a token can be used in conjunction with the ``refresh_token`` keyword argument
using in initializing an instance of :class:`~praw.Reddit`. A list of all possible
scopes can be found in the `reddit API docs <https://www.reddit.com/dev/api/oauth>`_

.. literalinclude:: ../examples/obtain_refresh_token.py
   :language: python
