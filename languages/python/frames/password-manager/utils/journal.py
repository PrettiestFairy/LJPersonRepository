# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-15 00:43:38 UTC+08:00
"""

import logging

from fairylandfuture.modules.journal import Journal

journal: Journal = Journal(serialize=True)
# journal: Journal = Journal(debug=True, serialize=True)


class JournalHandler(logging.Handler):
    def emit(self, record):
        message = self.format(record)
        if record.levelno >= logging.CRITICAL:
            journal.critical(message)
        elif record.levelno >= logging.ERROR:
            journal.error(message)
        elif record.levelno >= logging.WARNING:
            journal.warning(message)
        elif record.levelno >= logging.INFO:
            journal.info(message)
        elif record.levelno >= logging.DEBUG:
            journal.debug(message)
