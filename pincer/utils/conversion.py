# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client
    from .types import T, MISSING
    from typing import Dict, Callable, Any, Optional


def construct_client_dict(client: Client, data: Dict[...]):
    return {
        **data,
        "_client": client,
        "_http": client.http
    }


def convert(
        value: Any,
        factory: Callable[[Any], T],
        check: Optional[type] = None,
        client: Optional[Client] = None
) -> T:
    def handle_factory() -> T:
        def fin_fac(v: Any):
            if check is not None and isinstance(v, check):
                return v

            if client is None:
                return factory(v)

            return factory(construct_client_dict(client, v))

        return (
            list(map(fin_fac, value))
            if isinstance(value, list)
            else fin_fac(value)
        )

    return MISSING if value is MISSING else handle_factory()
