# script that erases files path.txt and tasks_app.md
def erase():
    import os
    os.remove('path.txt')
    print('files erased')
    return
erase()