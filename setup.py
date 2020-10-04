from distutils.core import setup
import glob

setup(
    name='blog',
    version='0.1',
    author='Yinjia',
    author_email='liyinjia0452@gmail.com',
    description='django blog',
    url='',
    packages=['blog', 'user', 'post'],
    data_files=glob.glob('template/*.html') + ['requirements', 'manage.py']

)
