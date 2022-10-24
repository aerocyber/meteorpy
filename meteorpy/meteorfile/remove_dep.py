import json
import os
from meteorpy.meteorfile import io as read_write

def add(dependency: str, meteorfile_path: str = os.path.join(os.getcwd(), 'meteorfile'))-> None:
    """
        meteorpy/meteorfile/remove_dep.py#validate_meteorfile
        =============================================

        About
        =====
        Remove a dependency to meteorfile.

        Accepts
        =======
        dependency: string (str): The dependency to be removed.
        meteorfile_path: string (str): The path to meteorfile. : Default: os.path.join(os.getcwd(), 'meteorfile')

        Return
        ======

        [Type]
        ======
        None

    """
    _dat = read_write.read_meteorfile(meteorfile_path, meteorfile_path)
    deps: list = _dat["Dependencies"]
    for dep in deps:
        if (dep == dependency):
            _dat["Dependencies"].remove(dep)
    read_write.write_meteorfile(json.dump(_dat), meteorfile_path)