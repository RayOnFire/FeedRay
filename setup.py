from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-user',
        'flask-sqlalchemy',
        'flask-admin',
        'flask-restful',
        'flask-login',
        'pagan'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)