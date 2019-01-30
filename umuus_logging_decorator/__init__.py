#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Jun Makii <junmakii@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""Utilities, tools, and scripts for Python.

umuus-logging-decorator
=======================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-logging-decorator.git

Example
-------

    $ umuus_logging_decorator

    >>> import umuus_logging_decorator


----

    $ export BETTER_EXCEPTIONS=1

----


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

"""
import sys
import functools
import toolz
import attr
import loguru
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-logging-decorator'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__author_username__ = 'junmakii'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'attrs>=18.2.0',
    'toolz>=0.9.0',
    'loguru>=0.2.5',
    'better_exceptions>=0.2.2',
]
__dependency_links__ = []
__classifiers__ = []
__entry_points__ = {}
__project_urls__ = {}
__setup_requires__ = []
__test_suite__ = ''
__tests_require__ = []
__extras_require__ = {}
__package_data__ = {}
__python_requires__ = ''
__include_package_data__ = True
__zip_safe__ = True
__static_files__ = {}
__extra_options__ = {}
__download_url__ = ''
__all__ = []


@attr.s()
class Logger(object):
    def __attrs_post_init__(self):
        loguru.logger.configure(handlers=[{
            "sink":
            sys.stdout,
            "colorize":
            True,
            "format":
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>"
        }])

    def truncate(self, s, max_length=255, end='...'):
        return (len(s) > max_length and s[:max_length] + end or s)

    @toolz.curry
    def decorator(self, fn, level='INFO'):
        module = (getattr(fn, '__module__', None) and fn.__module__ or '')
        qualname = (getattr(fn, '__qualname__', None) and fn.__qualname__
                    or '')
        name = (module + '.' + qualname)
        logger = getattr(loguru.logger, level.lower())

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            logger(self.truncate('{name}'.format(**dict(locals(), name=name))))
            try:
                result = fn(*args, **kwargs)
                logger(
                    self.truncate('{name}\tresult\t{result}'.format(
                        **dict(locals(), name=name))))
                return result
            except Exception as err:
                raise err

        return wrapper


logger = Logger()
