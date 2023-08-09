import shutil

def clear_from_local(cwd):
  shutil.rmtree(f"{cwd}/images", ignore_errors=False, onerror=None, dir_fd=None)