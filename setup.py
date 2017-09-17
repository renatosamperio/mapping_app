import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'e')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mapping_app',
    version='0.1',
    author='Renato Samperio',
    author_email='renatosamperio@gmail.com',
    url='https://github.com/renatosamperio/mapping_app',
    description='Use a google map to store pointsz',
    long_description=README,
    license='BSD',
    packages=['gmap_app'],
    package_data={'gmap_app': ['templates/gmap_app/*']},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5.2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
