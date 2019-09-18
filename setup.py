from setuptools import setup

setup(
   name='TimeManager',
   version='1.0',
   description='Application with GUI that allows you to track the time spent at the workplace',
   author='Zamaschikov Yaroslav',
   author_email='theyak73@gmail.com',
   url='https://github.com/Yak73/TimeManager.git',
   packages=['TimeManager'],  
   install_requires=['PyQt5', 'pyodbc', 'datetime', 'sys', 'inspect'], 
)
