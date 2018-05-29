import os.path


BASE_PATH = os.path.abspath(os.path.dirname(__file__))


def get_local_path(name):
    dest = os.path.normpath(os.path.join(BASE_PATH, os.path.join(name)))
    if not dest.startswith(BASE_PATH):
        raise ValueError

    return dest


def open_local(name, *args, **kwargs):
    return open(get_local_path(name), *args, **kwargs)

