import os
import logging
logger = logging.getLogger()

def get_file_path_or_content(path, content=None):
	working_dir = (os.path.dirname(__file__)).split("src")[0]
        file_path = os.path.join("\\".join(working_dir.split("\\")),
                                 "\\".join((path.replace("\\", "/").split("\\"))))
        if os.path.exists(file_path):
            if content:
                with open(file_path) as f:
                    data = f.read()
                return json.loads(data)
            else:
                return file_path
        else:
            raise logging.error(f"{file_path} file not found exception")
