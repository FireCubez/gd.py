__title__ = 'gd'
__author__ = 'NeKitDSS'
__copyright__ = 'Copyright 2019 NeKitDSS'
__license__ = 'MIT'
__version__ = '0.7.0b1'

from collections import namedtuple
import logging

from .abstractentity import AbstractEntity
from .abstractuser import AbstractUser
from .comment import Comment
from .errors import *
#from .level import Level
from .message import Message
from .song import Song
from .unreguser import UnregisteredUser
from .user import User
from .graphics.colors import Color, colors
from .utils.captcha_solver import Captcha
from .utils.gdpaginator import Paginator
from .utils.crypto.coders import Coder
from .utils.crypto.xor_cipher import XORCipher as xor
from .client import Client

def _gen_version_details():
    ver = __version__
    cases = {
        'a' in ver: ('a', 'alpha'),
        'b' in ver: ('b', 'beta'),
        'rc' in ver: ('rc', 'candidate')
    }
    # we should not care about the separator if the releaselevel is 'final'
    splitter, releaselevel = cases.get(True, (' ', 'final'))
    splitted = ver.split(splitter)
    serial = 0
    if len(splitted) > 1:  # if there's a serial
        _, s = splitted
        serial = int(s)
    major, minor, micro = map(int, splitted[0].split('.'))
    VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
    return VersionInfo(
        major=major, minor=minor, micro=micro, releaselevel=releaselevel, serial=serial
    )
    
version_info = _gen_version_details()


def setup_basic_logging():
    """Function that sets up logs of the module,
    with the following format:
    [INFO] (time) {gd.some_module}: Some info message.
    """
    log = logging.getLogger(__name__)
    hdlr = logging.StreamHandler()
    hdlr.setFormatter(
        logging.Formatter('[%(levelname)s] (%(asctime)s) {%(name)s}: %(message)s')
    )
    log.setLevel(logging.INFO)
    log.addHandler(hdlr)

# setting up the NullHandler here
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
