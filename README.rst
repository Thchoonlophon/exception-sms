Exception-Sms
=============

This package is used to notify developer that program catched a
exception, Once this mechanism is triggered, the developer is
notified via text message, along with the general reason for
the exception and the function that caused it. At the same time,
the package generates log files locally for developers to read
and check for exceptions.

How to Install
--------------

You can install this package by execute the command like this
``pip install exception-sms`` in command line. One important thing
is that this package only support Python3.6 or higher versions.

Examples
--------

How to use it:

.. code-block:: python

    from exception_sms import GetNotification

    logs = GetNotification(
        "Your access_key",
        "Your secret_key",
        "Your template_id of sms",
        "The author of the function",
        "Receiver's Phone number",
        "The path of log files"
    )

    @log.exce_note
    def tests_func(x, y):
        out = x / y
        return out


    if __name__ == "__main__":
        result = tests_func(0, 0)
        print(result)

The result of the code above:

.. image:: https://file.lynchow.com/jingxuan/20200710/Awf8anosxXLB.png

.. image:: https://file.lynchow.com/jingxuan/20200710/ydqGsHkot9aG.png