
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def run_tests(self):
        import sys
        import shlex
        import pytest
        errno = pytest.main(['--doctest-modules'])
        if errno != 0:
            raise Exception('An error occured during installution.')
        install.run(self)


setup(
    packages=setuptools.find_packages('.'),
    version='0.1',
    url='https://github.com/junmakii/umuus-logging-decorator',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['attrs>=18.2.0', 'toolz>=0.9.0', 'loguru>=0.2.5'],
    dependency_links=[],
    classifiers=[],
    entry_points={},
    project_urls={},
    setup_requires=[],
    test_suite='',
    tests_require=[],
    extras_require={},
    package_data={},
    python_requires='',
    include_package_data=True,
    zip_safe=True,
    download_url='',
    name='umuus-logging-decorator',
    description='Utilities, tools, and scripts for Python.',
    long_description=('Utilities, tools, and scripts for Python.\n'
 '\n'
 'umuus-logging-decorator\n'
 '=======================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install '
 'git+https://github.com/junmakii/umuus-logging-decorator.git\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 '    $ umuus_logging_decorator\n'
 '\n'
 '    >>> import umuus_logging_decorator\n'
 '\n'
 '\n'
 '\n'
 '    class Foo:\n'
 "        @umuus_logging_decorator.logger.decorator(level='WARNING')\n"
 '        def bar(self, *args, **kwargs):\n'
 "            return 'OK'\n"
 '\n'
 '    @umuus_logging_decorator.logger.decorator()\n'
 '    def test_fn(x, y):  # type: None\n'
 '        return x * y\n'
 '\n'
 '    test_fn(1, 2)\n'
 '    Foo().bar(1, 2, 3, x=1, y=1)\n'
 '\n'
 '    ### Output\n'
 '\n'
 '    2019-01-30 20:34:04.893 | INFO     | __main__.test_fn   input   (1, 2)  '
 '{}\n'
 '    2019-01-30 20:34:04.893 | INFO     | __main__.test_fn   result  2\n'
 '    2019-01-30 20:34:04.893 | WARNING  | __main__.Foo.bar   input   '
 "(<__main__.Foo object at 0x7f559560b780>, 1, 2, 3)      {'x': 1, 'y': 1}\n"
 '    2019-01-30 20:34:04.894 | WARNING  | __main__.Foo.bar   result  OK\n'
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    cmdclass={"pytest": PyTest},
)
