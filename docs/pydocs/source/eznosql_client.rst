=================
``EzNoSQLClient``
=================

.. important::
    A client instance manages a connection token and provides context
    management functionality using :meth:`~.__enter__` and :meth:`~.__exit__`
    methods. Please note that only one active connection is supported per
    client, and all member functions require a valid database connection.

    Additional connections can be established as needed by creating
    multiple EzNoSQLClient instances with different options, or to load
    balance the workload. Each connection allows for 1024 concurrent
    read/write requests.

    If opting to manage connection tokens manually, a client connection
    should be terminated by using the :meth:`~.znsq_close` method

.. autoclass:: pyeznosql.client.EzNoSQLClient
    :members:
    :special-members: __init__, __enter__, __exit__