import os


def add_gitignore(path_to_gitignore: str, meteorpy_venv_name: str = 'venv') -> None:
    """
        meteorpy/env_setup/clean_env.py
        =============================================

        About
        =====
        Add meteorpy related dir to .gitignore file.

        Accepts
        =======
        path_to_gitignore: string (str): The path to the gitignore file. Can be existing or not.
        meteorpy_venv_name: string (str): The name of the directory which hosts the venv used by meteorpy. Default: Uses venv dir.

        Return
        ======

        [Type]
        ======
        None

    """
    DEFAULT_GITIGNORE = ['__pycache__/', '*.py[cod]', '*$py.class', '*.so', '.Python',
     'build/', 'develop-eggs/', 'dist/', 'downloads/', 'eggs/', '.eggs/', 'lib/', 'lib64/',
     'parts/', 'sdist/', 'var/', 'wheels/', 'share/python-wheels/', '*.egg-info/', 
     '.installed.cfg', '*.egg', 'MANIFEST', '*.manifest', '*.spec', 'pip-log.txt', 
     'pip-delete-this-directory.txt', 'htmlcov/', '.tox/', '.nox/', '.coverage', 
     '.coverage.*', '.cache', 'nosetests.xml', 'coverage.xml', '*.cover', '*.py,cover', 
     '.hypothesis/', '.pytest_cache/', 'cover/', '*.mo', '*.pot', '*.log', 'local_settings.py', 
     'db.sqlite3', 'db.sqlite3-journal', 'instance/', '.webassets-cache', '.scrapy', 
     'docs/_build/', '.pybuilder/', 'target/', '.ipynb_checkpoints', 'profile_default/', 
     'ipython_config.py', '.pdm.toml', '__pypackages__/', 'celerybeat-schedule', 
     'celerybeat.pid', '*.sage.py', '.env', '.venv', 'env/', 'venv/', 'ENV/', 'env.bak/', 
     'venv.bak/', '.spyderproject', '.spyproject', '.ropeproject', '/site', '.mypy_cache/', 
     '.dmypy.json', 'dmypy.json', '.pyre/', '.pytype/', 'cython_debug/'] # Gitignore for Python taken from: https://github.com/github/gitignore/blob/main/Python.gitignore Commit: 8e67b9420cb6796e5eeca72682babdb06627ec8c Commit URL: https://github.com/github/gitignore/commit/8e67b9420cb6796e5eeca72682babdb06627ec8c
    
    METEORPY_GITIGNORE = meteorpy_venv_name

    if (os.path.exists(path_to_gitignore)):
        f = open(path_to_gitignore, 'r')
        _gitignore = f.read().split('\n')
        f.close()
        if (METEORPY_GITIGNORE in _gitignore):
            return
        else:
            _gitignore.append(METEORPY_GITIGNORE)
            f = open(path_to_gitignore, 'w')
            f.writelines(_gitignore)
            f.flush()
            f.close()
    else:
        DEFAULT_GITIGNORE.append(METEORPY_GITIGNORE)
        f = open(path_to_gitignore,'w')
        f.writelines(DEFAULT_GITIGNORE)
        f.flush()
        f.close()