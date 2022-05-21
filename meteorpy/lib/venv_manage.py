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

import venv
import os.path
import os
import sys
import subprocess


class EnvCreationError(Exception):
    pass


class BuildEnv(venv.EnvBuilder):
    def __init__(self, path, with_pip, system_site_packages, prompt, clear, upgrade, upgrade_deps, requirements, install_requirements):
        self.path = os.path.normcase(
            os.path.normpath(
                path
            )
        )
        self.with_pip = with_pip
        self.system_site_packages = system_site_packages
        if os.name == 'nt':
            self.symlinks = False
        else:
            self.symlinks = True
        self.prompt = prompt
        self.clear = clear
        self.upgrade = upgrade
        self.upgrade_deps = upgrade_deps
        self.requirements = requirements
        self.install_requirements = install_requirements

    
    def add_requirements(self, requirements: list):
        self.requirements = requirements
    

    def upgrade(self):
        self.upgrade = True
    

    def upgrade_deps(self):
        self.upgrade_deps = True


    def allow_site_packages(self):
        self.system_site_packages = True
    

    def clear_dir(self):
        self.clear = True


    def prompt(self, new_prompt):
        self.prompt = new_prompt # Use None for default venv behaviour.


    def no_upgrade(self):
        self.upgrade = False
    

    def no_upgrade_deps(self):
        self.upgrade_deps = False


    def disallow_site_packages(self):
        self.system_site_packages = False
    

    def no_clear_dir(self):
        self.clear = False


    def no_install_requirements(self):
        if self.requirements:
            raise EnvCreationError("Requirements exists. Can't stop installation if requirements exist.")
        self.install_requirements = False
    

    def nopip(self):
        if self.requirements:
            raise EnvCreationError("Requirements exists. Can't stop installation of pip if requirements exist.")
        self.with_pip = False

    
    def apply(self):
        if os.path.exists(self.path) and not self.clear:
            raise TargetExistsError(self.path + " exists.")
        if self.upgrade and self.clear:
            raise ValueError("Cannot use clear and upgrade together.")
        

    def post_setup(self, context):
        for i in self.requirements:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])

def build(path, with_pip = True, system_site_packages = False, prompt = False, 
clear = False, upgrade = False, upgrade_deps = False, requirements = [], install_requirements = True):
    path = os.path.abspath(path)
    if not prompt:
        if os.path.isfile(path):
            path = os.path.dirname(path)
        prompt = "Aurora:: " + path
    builder = BuildEnv(path, with_pip, system_site_packages, prompt, clear, upgrade, upgrade_deps, requirements, install_requirements)
    