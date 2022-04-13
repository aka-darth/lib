import json
import os

env = os.environ.get('PY_ENV', '')

print(env)

def getconfig():
    filename = 'src/config.json'
    f = open(filename, 'r')
    c = json.loads(f.read())
    f.close()
    return c