from fabric.api import *

"""
install fab
Note: this is a fork of fabric, which is not maintained anymore.
Note: run this fabric only once on start a new project
# pip install git+https://github.com/ahmedyasserays/fabric.git@ff01d6b7c65ca6477261a92765e25b5f36fa8dfa
"""
def run():
    run('python3 -m venv venv')
    run('source venv/bin/activate')
    run('pip3 install -r requirements.txt')
    run('python3 manage.py migrate --noinput')
    run('python3 manage.py collectstatic --noinput')
    run('python3 manage.py createsuperuser')
    run('python3 manage.py runserver')
