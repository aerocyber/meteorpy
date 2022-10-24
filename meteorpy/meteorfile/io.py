import os
import json
from jsonschema import ValidationError, validate


def validate_meteorfile(meteorfile_content: str)-> bool:
    """
        meteorpy/meteorfile/io.py#validate_meteorfile
        =============================================

        About
        =====
        Check if a given meteorfile content is valid or not.

        Accepts
        =======
        meteorfile_content: string (str): The content of meteorfile.

        Return
        ======

        [Type]
        ======
        Bool

        [When]
        ======
        True: if the meteorfile_content is valid.
        False: if the meteorfile_content is invalid.

    """
    schema = {
        "type": "object",
        "properties": {
            "Dependencies": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        {
                            "type": "string"
                        }: {
                            "type": "string"
                        }
                    }
                }
            },
            "Relative environment path": {
                "type": "string"
            }
        }
    }
    try:
        _dat = json.loads(meteorfile_content)
    except ValueError:
        return False
    else:
        try:
            validate(instance=_dat, schema=schema)
        except ValidationError:
            return False
        else:
            return True
        

def read_meteorfile(meteorfile_path: str = os.path.join(os.getcwd(), 'meteorfile'))-> str:
    """
        meteorpy/meteorfile/io.py#read_meteorfile
        =============================================

        About
        =====
        Read and return meteorfile data.

        Accepts
        =======
        meteorfile_path: string (str): The path to meteorfile. : Default: os.path.join(os.getcwd(), 'meteorfile')

        Return
        ======

        [Type]
        ======
        None

    """
    if (not os.path.exists(meteorfile_path)):
        raise FileNotFoundError(meteorfile_path + " does not exist.")
    
    f = open(meteorfile_path, 'r')
    _data = f.read()
    f.close()

    if (not validate_meteorfile(_data)):
        raise ValidationError("Invalid meteorfile content.")
    
    return json.loads(_data)


def write_meteorfile(meteorfile_content: str, meteorfile_path: str = os.path.join(os.getcwd(), 'meteorfile'))-> None:
    """
        meteorpy/meteorfile/io.py#write_meteorfile
        =============================================

        About
        =====
        Write meteorfile data.

        Accepts
        =======
        meteorfile_path: string (str): The path to meteorfile. : Default: os.path.join(os.getcwd(), 'meteorfile')
        meteorfile_content: string (str): The content to write.

        Return
        ======

        [Type]
        ======
        None

    """ 

    if (not validate_meteorfile(meteorfile_content)):
        raise ValidationError("Invalid meteorfile content.")
    
    f = open(meteorfile_path, 'w')
    f.write(write_meteorfile)
    f.close()

