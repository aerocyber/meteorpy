import os
import shutil

def clean_up(dir: str) -> None:
    """
        meteorpy/env_setup/clean_env.py
        =============================================

        About
        =====
        Clean an environment created for the project.

        Accepts
        =======
        dir: string (str): The path to be cleaned.

        Return
        ======

        [Type]
        ======
        None

    """

    ENV_PATH = os.path.normcase(os.path.normpath(os.path.abspath(dir)))
    shutil.rmtree(ENV_PATH)
