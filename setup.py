from setuptools import setup


setup(
    name='pv', #Asi es como invocar la linea de comandos
    version='0.1',
    py_modules=['pv'], #Se va a llamar al modulo pv
    install_requires=[ #Requisitos de la aplicacion
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''', # Punto de entrada de nuestra aplicación
)