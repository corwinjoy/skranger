import os
import shutil

top = os.path.dirname(os.path.abspath(__file__))


def copy_ranger_source():
    """Copy the ranger cpp source, following symlinks."""
    src = os.path.join(top, "ranger", "cpp_version")
    dst = os.path.join(top, "skranger", "ranger")
    try:
        shutil.rmtree(dst)
    except FileNotFoundError:
        pass
    shutil.copytree(src, dst, symlinks=False)


copy_ranger_source()
