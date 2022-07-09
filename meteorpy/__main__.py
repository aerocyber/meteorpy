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

from platform import python_version, system
import json
import os
import click
from API import get_deps, get_python, get_remote_python, meteorfile, venv_manage

# Commands and groups:
#
# Group: create: Create meteorfile


@click.command("create")
@click.option('--path', '-p', 'path', default='./venv/', help="Path where virtual environment is to be created. Relative path.", show_default=True, required=True)
@click.option('--python-version', 'python', default=python_version(), help="Python version to lock", show_default=True, required=True)
@click.option('--with-pip', '-P', 'with_pip', is_flag=True, default=True, help="With pip support", show_default=True)
@click.option('--system-site-packages', '-S', 'system_site_packages', is_flag=True, default=False, help="Allow access to system site packages.", show_default=True)
@click.option('--prompt', 'prompt', default=False, help="Prompt for venv.", show_default=True)
@click.option('--clear', '-c', 'clear', is_flag=False, default=True, help="Clear the target dir if exists", show_default=True)
@click.option('--upgrade', '-U', 'upgrade', is_flag=True, default=True, help="Upgrade existsing venv if found.", show_default=True)
@click.option('--upgrade-deps', '-u', 'upgrade_deps', is_flag=True, default=True, help="Upgrade dependencies to latest version.", show_default=True)
@click.option('--install-requirements', '-i', is_flag=True, default=True, help="Install requirements.", show_default=True)
@click.option('--requirements', '-r', 'requirements', default=[], type=[], help="Requirements in Python's list format", show_default=True)
def create(path, python, with_pip, system_site_packages, prompt, clear, upgrade, upgrade_deps,
 requirements, install_requirements):
 """
     Create Meteorfile.
 """
 if upgrade and clear:
    click.echo("Upgrade (--upgrade/-U) and clear (--clear/-c) flags cannot be used together.")
 meteorfile = meteorfile.create_file_contents(with_pip, path, system_site_packages, prompt, clear, upgrade, upgrade_deps, requirements, install_requirements)
 f = open(os.path.join(os.getcwd(), 'Meteorfile'), 'w')
 f.write(json.dumps(meteorfile))
 f.close()
 click.echo("Meteorfile created")


@click.command("recreate")
@click.option('--meteorfile', '-m', 'meteorpath', default='./Meteorfile', required=True, show_default=True, help="Path to Meteorfile")
def env(meteorpath):
    """ 
        Recreate virtual environment using Meteorfile.
    """
    f = open(meteorpath)
    config = json.loads(f.read())
    f.close()
    click.echo("Loaded Meteorfile config file.\nCreating virtual environment from Meteorfile.")
    path = config['path']
    with_pip = config['with_pip']
    system_site_packages = config['system_site_packages']
    prompt = config['prompt']
    clear = config['clear']
    upgrade = config['upgrade']
    upgrade_deps = config['upgrade_deps']
    requirements = config['requirements']
    install_requirements = config['install_requirements']
    venv_manage.build(path, with_pip, system_site_packages, prompt, clear, upgrade, upgrade_deps, requirements, install_requirements)
    click.echo("Created environment.")
    if system() == 'Linux':
        cmd = '. {p}/bin/activate'.format(p=path)
    elif system() == 'Windows':
        cmd = '.\\{p}\\bin\\activate.bat'.format(p=path)


if __name__ == '__main__':
    env()