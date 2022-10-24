import json
import os
from meteorpy.meteorfile import io as read_write

def add(dependency: str, version: str, meteorfile_path: str = os.path.join(os.getcwd(), 'meteorfile'))-> None:
    """
        meteorpy/meteorfile/add.py
        =============================================

        About
        =====
        Add a dependency to meteorfile.

        Accepts
        =======
        dependency: string (str): The dependency to be added.
        version: string (str): The version of the dependency to be added.
        meteorfile_path: string (str): The path to meteorfile. : Default: os.path.join(os.getcwd(), 'meteorfile')

        Return
        ======

        [Type]
        ======
        None

    """
    _dat = read_write.read_meteorfile(meteorfile_path, meteorfile_path)
    _dat["Dependencies"].append({dependency: version})
    read_write.write_meteorfile(json.dump(_dat), meteorfile_path)