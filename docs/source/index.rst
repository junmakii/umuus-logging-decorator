
umuus-logging-decorator
=======================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-logging-decorator.git

Example
-------

    $ umuus_logging_decorator

    >>> import umuus_logging_decorator



    class Foo:
        @umuus_logging_decorator.logger.decorator(level='WARNING')
        def bar(self, *args, **kwargs):
            return 'OK'

    @umuus_logging_decorator.logger.decorator()
    def test_fn(x, y):  # type: None
        return x * y

    test_fn(1, 2)
    Foo().bar(1, 2, 3, x=1, y=1)

    ### Output

    2019-01-30 20:34:04.893 | INFO     | __main__.test_fn   input   (1, 2)  {}
    2019-01-30 20:34:04.893 | INFO     | __main__.test_fn   result  2
    2019-01-30 20:34:04.893 | WARNING  | __main__.Foo.bar   input   (<__main__.Foo object at 0x7f559560b780>, 1, 2, 3)      {'x': 1, 'y': 1}
    2019-01-30 20:34:04.894 | WARNING  | __main__.Foo.bar   result  OK

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>

Table of Contents
-----------------
.. toctree::
   :maxdepth: 2
   :glob:

   *

