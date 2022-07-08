import json
import os
import logging
import sys

logger = logging.getLogger()


def getPathOrContent(path, content=True):
    if sys.platform in ['linux', 'darwin']:
        print("from Darwin")
        name = ((os.path.dirname(__file__)).split("/"))[::-1][1]
    else:
        print("from Windows")
        name = ((os.path.dirname(__file__)).split("\\"))
    print(f"name = %s" % name)
    working_dir = (os.path.dirname(__file__)).split(name)[0] + name
    print(working_dir)
    file_path = os.path.join("\\".join(working_dir.split("\\")), 'Data',
                             "\\".join((path.replace("\\", "/").split("\\"))))
    print(file_path)
    if os.path.exists(file_path):
        if content:
            with open(file_path, 'r+') as f:
                try:
                    data = json.load(f)
                    return data
                except Exception as e:
                    logger.exception(e)
        else:
            return file_path
    else:
        raise logging.error(f"{file_path} file not found exception")
