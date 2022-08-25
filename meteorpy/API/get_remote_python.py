# Get Python for installation
# Copyright © 2022 aerocyber

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the “Software”), to deal in the Software without
# restriction, including without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import platform
import subprocess
import sys
import requests


class URLError(Exception):
    pass


BASE_URL = "https://www.python.org/ftp/python/"

def dwnl_python(target_path, version=platform.python_version(), download_target=platform.system()):
    """ 
        Download python for target OS
    """
    if download_target == 'Windows':
        url_modifier = version + '/' + 'python-' + version + '-amd64.exe'
        commands = [
            'python-' + version + '-amd64.exe' + '/passive InstallAllUsers=0 TargetDir=' + os.path.join(os.getcwd(), 'venv', 'python-' + version) + 'AssociateFiles=0 Shortcuts=0 Include_doc=0 Include_launcher=0 InstallLauncherAllUsers=0'
        ]
    elif download_target == 'Linux':
        url_modifier = version + '/' + 'Python-' + version + '.tgz'
        commands = ['cd ' + target_path,
        'tar xf Python-' + version + '.tgz', 'cd Python-' + version,
        './configure --prefix $HOME/.meteorpy/python-' + version + '/',
        'make altinstall'
        ]
    else:
        raise NotImplementedError("The target platform:\t" + download_target + ", is not supported by meteorpy.")
    URL = BASE_URL + url_modifier
    if requests.get(URL).status_code == 404:
        raise URLError("Invalid version string")
    else:
        r = requests.get(URL, stream=True)
        if r.status_code == 200:
            with open(os.path.join(target_path, URL.split('/')[-1])) as f:
                f.write(r.raw.read())
    for i in commands:
        _cmd = commands.split(' ')
        _out = subprocess.run(_cmd, capture_output=True)
        if _out:
            sys.stdout.write(_out)