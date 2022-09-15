# Copyright (c) 2022 aerocyber
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import os
import requests
import meteorpy.api.versions # Because versions return a list of versions and the code logicc makes sense.


class InvalidVersionException(Exception):
    ...

class VersionsListEmpty(Exception):
    ...



def get_url(version: str):
    """Get Python download URL.

    Args:
        version (str): Version to download.
    """
    if version:
        try:

            if meteorpy.api.versions.versions == []:
                raise 
            if version not in meteorpy.api.versions.versions.keys():
                raise NotImplementedError(f"The version {version} is not implemented.") # Filter out unsupported versions.

            return f"http://www.python.org/ftp/python/%(base_version)/Python-%(version).tgz" # Return the url for download.
        except:
            raise VersionsListEmpty("The versions_list is empty due to exception.")
    else:
        raise InvalidVersionException("version cannot be empty.")


def download(url: str):
    """Download python source.

    Args:
        url (str): The URL to the source distribution.
    """
    cwd = os.getcwd()
    filename = url.split('/')[-1] # Get split the url, select the last element. That's the file name.
    filename = os.path.join(
        os.path.expanduser("~"),
        ".meteorpy",
        "src",
        filename
    ) # Change the filename to the complete path.

    _response = requests.get(url, allow_redirects=True) # Get the url content.
    filename.writebytes(_response.content) # Write it to the file.