from setuptools import setup

setup(
    name="pytest_bugzilla",
    version="0.1",
    description='py.test bugzilla integration plugin',
    long_description=open('README.txt').read(),
    license='GPL',
    author='Noufal Ibrahim',
    author_email='noufal@nibrahim.net.in' ,
    url='',
    platforms=['linux', 'osx', 'win32'],
    py_modules=['pytest_bugzilla'],
    entry_points = {'pytest11': ['pytest_bugzilla = pytest_bugzilla'],},
    zip_safe=False,
    install_requires = ['PyZilla','py>=1.1.1'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Topic :: Software Development :: Testing',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Utilities',
    'Programming Language :: Python',
    ],
)
