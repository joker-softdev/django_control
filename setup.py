from setuptools import find_packages, setup

setup(
    name='django-controlcenter',
    version='0.2.0',
    description='Set of widgets to build dashboards for your Django-project.',
    long_description='',
    url='https://github.com/byashimov/django-controlcenter',
    author='Murad Byashimov',
    author_email='byashimov@gmail.com',
    packages=find_packages(
        exclude=['controlcenter.stylus', 'controlcenter.images']),
    include_package_data=True,
    license='BSD',
    install_requires=['django-pkgconf'],
    keywords='django admin dashboard',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
)
