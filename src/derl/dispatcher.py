#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

from logging import getLogger
from requests import get, Timeout, TooManyRedirects

_logger = getLogger(__name__)

_DEFAULT_TIMEOUT = 10


def request(files, timeout=_DEFAULT_TIMEOUT):
    if len(files) == 0:
        _logger.debug("No matches for HTTP requests")
        return []

    for current_file in files:
        for current_url in current_file.urls:
            try:
                _logger.debug("Requesting status code for %s", current_url.url)
                current_url.status_code = get(current_url.url, timeout=timeout).status_code
            except ConnectionError:
                _logger.debug("Connection Error occurred while getting %s", current_url.url)
            except Timeout:
                _logger.debug("Waited for %i seconds, giving up getting %s", timeout, current_url.url)
            except TooManyRedirects:
                _logger.debug("Redirection Tango, danced enough with %s", current_url.url)

    return files
