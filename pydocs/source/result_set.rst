=============
``ResultSet``
=============
.. important::
    A ResultSet instance manages a result token and provides context
    management functionality using :meth:`~ResultSet.__enter__` and
    :meth:`~ResultSet.__exit__` methods. Please note that only one
    active result token is supported per instance, and all member
    functions require a valid database connection and result token.
    For this reason, the user is discouraged from directly invoking
    the `ResultSet.__init__()` constructor. Instead, use the
    :meth:`~.znsq_position` factory method to instantiate a ResultSet.

    If opting to manage result tokens manually, positioning should be
    terminated by using the :meth:`~.znsq_close_result` to release a result token.


.. autoclass:: pyeznosql.resultset.ResultSet
    :members: znsq_close_result, znsq_delete_result, znsq_next_result, znsq_replace_result
    :special-members: __enter__, __exit__
    :exclude-members: __init__, __weakref__, __new__