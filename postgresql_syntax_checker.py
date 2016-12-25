import os
import shlex
import subprocess

import shortuuid


def postgresql_syntax_checker(line, query=''):
    file_path = '{}.sql'.format(shortuuid.uuid())

    with open(file_path, 'w') as f:
        f.write(query)

    cmd = 'pgsanity {}'.format(file_path)
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    output = proc.stdout.read()

    output = output if output else 'Valid Syntax'
    os.remove(file_path)
    return output


postgresql_syntax_checker('afs', 'select s* from t;')


def load_ipython_extension(ipython):
    ipython.register_magic_function(postgresql_syntax_checker, 'cell', 'postgresql_syntax_checker')
