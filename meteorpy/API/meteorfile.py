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


from json import loads
from jsonschema import validate

class ConfigError(Exception):
    pass

class FormatError(Exception):
    pass


def create_file_contents(py_version: str, path: str, deps: str, py_lock: bool = True, rel_path: str = './.venv/', with_pip: bool = True, system_site_packages: bool = False, prompt: str = '', 
clear: bool = False, upgrade: bool = False, upgrade_deps: bool = False, install_requirements: bool = True) -> dict:
    """
        Create the content for Meteorfile.
        py_version[str]: Version of Python to lock. Pass 'None' with py_lock=False to disable.
        deps[str]: Output of `pip freeze` command as it is.
        py_lock[bool]: Whether to lock python or not.
    """
    meteor_content = {
        "Lock Python": py_lock
    }
    if not py_lock and py_version == 'None':
        meteor_content["Lock Python Version"] = ''
    elif (py_lock and py_version == 'None') or (not py_lock and py_version != 'None'):
        raise ConfigError("Values of py_lock and py_version conflict each other.")
    else:
        meteor_content["Lock Python Version"] = py_version
    meteor_content["path"] = path
    meteor_content["Dependencies"] = deps
    meteor_content['with_pip'] = with_pip
    meteor_content['system_site_packages'] = system_site_packages
    meteor_content['prompt'] = prompt
    meteor_content['clear'] = clear
    meteor_content['upgrade'] = upgrade
    meteor_content['upgrade_deps'] = upgrade_deps 
    meteor_content['install_requirements'] = install_requirements
    return meteor_content


def read_file_contents(content: str) -> dict:
    """
        Read content of Meteorfile.
        content[str]: Content of Meteorfile.
    """
    schema = {
        "type" : "object",
        "properties" : {
            "Lock Python" : {"type" : "string"},
            "Lock Python Version" : {"type" : "string"},
            "Dependencies": {"type": "string"},
            "path": {"type": "string"},
            "with_pip": {"type": "bool"},
            "system_site_packages": {"type": "bool"},
            "prompt": {"type": "string"},
            "clear": {"type": "bool"},
            "upgrade": {"type": "bool"},
            "upgrade_deps": {"type": "bool"},
            "install_requirements": {"type": "bool"},
        },
    }
    try:
        validate(instance=content, schema=schema)
    except Exception as e:
        raise FormatError("Invalid meteorfile format")
    else:
        return loads(content)
