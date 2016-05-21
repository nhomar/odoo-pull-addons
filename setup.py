from setuptools import setup

setup(
    name='Update Repositories from Config',
    version='1.0.2',
    py_modules=['update'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        odoo-pull-addons=update:cli
    ''',
)
