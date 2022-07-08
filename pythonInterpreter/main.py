try:
    from abc import ABC, abstractmethod
    import sys
    import subprocess
    if sys.version_info >= (3, 8):
        from importlib import metadata as importlib_metadata
    else:
        import importlib_metadata
except ImportError:
    raise ImportError


class Requirements(object):
    def checkImport(self, package):
        dists = importlib_metadata.distributions()
        return True if package in dists else self.install(package)

    def install(package):
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package])
        except:
            return False


class LanguageAbstract(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def varAuthenticate(self, var):
        pass

    @abstractmethod
    def funcAuthenticate(self, func):
        pass

    @abstractmethod
    def classAuthentcate(self):
        pass

    @abstractmethod
    def codeAuthenticate(self):
        pass


class Language(LanguageAbstract):
    def __init__(self, user):
        self.user = user

    def store(self, line):
        fn = None
        with open(fn, "a+"):
            fn.write(line)

    def varAuthenticate(self, line, variables):
        R = Requirements()
        # for gui
        allowedEntities = ["import", "def", "class",
                           "global", "if", "for", "while", "varNAME"]
        keywords = ["import", "def", "class", "global", "if", "for", "while"]
        i = line.split(' ')
        vars = v
        if i[0] in keywords:
            if i[0] == "import":
                boool = [mod.rstrip(",")
                         for mod in i[1:] if mod[len(mod)-1] == ","]
                for k in boool:
                    if R.checkImport(k) is False:
                        raise f"[*] Couldn't import package {k}"
                self.store(line)
            elif i[0] not in keywords:
                line1 = line.split("=")
                vars = [var.rstrip(",") for var in line1[0]]
                if "input(" in line1[1] and ")" == line1[len(line1[1].split('.')[0])-1]:
                    pass
                else:
                    vals = [vals.rstrip(",") for vals in line1[1]]
                    if not len(vars) == len(vals):
                        raise ValueError
                self.store(line1)
            elif i[0] == "class":
                pass

    def funcAuthenticate(self, i):
        if i[0] == chr(9):
            return i[1:]
        else:
            raise IndentationError

    def classAuthenticate(self, i):
        if i[0] == chr(9):
            return i[1:]
        else:
            raise IndentationError

    def codeAuthenticate(self, iLine):
        code = self.code
        classActive = False
        forLoopActive = False
        whileLoopActive = False
        variables = {}
        # int: {'a': 10, 'b': 20}, float: {'b': 10.0}, str: c, list: d, dict: e
        funcActive = False
        availableParam = []
        if classActive is True:
            i_ = self.classAuthenticate(iLine)
            if funcActive is True:
                i_ = self.funcAuthenticate(i_)
                self.varAuthenticate(i_, variables)

    def loopStdIn(self):
        for i in sys.stdin:
            self.codeAuthenticate(iLine=i)

# read the current line w.r.t previous line if not first line else validate first line
# for every next line repeat the previous line.


v = {
    "int": {},
    "float": {},
    "str": {},
    "dict": {},
    "list": {},
    "class": {},
    "func": {}
    }
