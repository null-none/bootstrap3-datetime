from setuptools import setup


setup(
    name='bootstrap3-datetime',
    packages=['bootstrap3_datetime',],
    package_data={'bootstrap3_datetime': ['static/bootstrap3_datetime/css/*.css',
                                          'static/bootstrap3_datetime/js/*.js',]},
    include_package_data=True,
    version='2.4',
    description='Bootstrap3 compatible datetimepicker for Django projects.',
    long_description=open('README.rst').read(),
    author='Nakahara Kunihiko',
    author_email='nakahara.kunihiko@gmail.com',
    url='https://github.com/gcaprio/django-bootstrap3-datetimepicker.git',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
