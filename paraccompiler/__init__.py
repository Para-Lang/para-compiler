""" Compiler for the Para-C programming language"""

__title__ = "parac-compiler"
__description__ = "Para-C compiler written in Python"
__url__ = "https://github.com/Luna-Klatzer/Para-C/"
__author__ = "Luna Klatzer"
__author_email__ = "luna.klatzer@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "v0.1"
__code_name__ = ""
__release__ = f"{__code_name__} {__version__}"
__copyright__ = "Luna Klatzer"


from .exceptions import __all__ as __exceptions_all__
from .exceptions import ParacCompilerError
from .exceptions import FilePermissionError
from .exceptions import AbortError
from .logger import __all__ as __logger_all__
from .logger import ParacFileHandler
from .logger import ParacFormatter
from .logger import log_traceback
from .logger import log_msg
from .logger import ParacStreamHandler
from .logger import ansi_col
from .logger import output_console
from .utils import __all__ as __utils_all__
from .utils import deprecated
from .compiler import DEFAULT_LOG_PATH
from .compiler import DEFAULT_BUILD_PATH
from .compiler import DEFAULT_DIST_PATH
from .compiler import ParacCompiler
from .compiler import CompilationProcess
from .__main__ import create_process
from .__main__ import cli
from .__main__ import parac_compile
from .__main__ import ParacCLI
from .__main__ import run_output_dir_validation
from .__main__ import run_process_with_formatting


__all__ = [
    '__title__',
    '__description__',
    '__url__',
    '__author__',
    '__author_email__',
    '__license__',
    '__version__',
    '__code_name__',
    '__release__',
    '__copyright__',
    *__exceptions_all__,
    *__utils_all__,
    *__exceptions_all__
]

import logging
import colorama

colorama.init(autoreset=True)
logging.getLogger(__name__).addHandler(logging.NullHandler())
