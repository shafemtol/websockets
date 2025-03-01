from __future__ import annotations

import warnings

# lazy_import doesn't support this use case.
from .protocol import SEND_EOF, Protocol as Connection, Side, State  # noqa


warnings.warn(
    "websockets.connection was renamed to websockets.protocol "
    "and Connection was renamed to Protocol",
    DeprecationWarning,
)
