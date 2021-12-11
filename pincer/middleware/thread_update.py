# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a thread is updated"""

from ..core.dispatch import GatewayDispatch
from ..objects import Channel
from ..utils import construct_client_dict, replace


async def thread_update_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for the ``on_thread_update`` event.

    Parameters
    ----------
    payload : :class:`~pincer.core.dispatch.GatewayDispatch`
        The data received from the thread update event.


    Returns
    -------
    Tuple[:class:`str`, :class:`~pincer.objects.guild.channel.Channel`]
        ``on_thread_update`` and an ``Channel``
    """

    channel = Channel.from_dict(construct_client_dict(self, payload.data))

    guild = self.guilds.get(channel.guild_id)

    if guild:
        guild.threads = replace(
            lambda _channel: _channel.id == channel.id,
            self.guilds[channel.guild_id].threads,
            channel
        )
        self.channels[channel.id] = channel

    return "on_thread_update", channel


def export():
    return thread_update_middleware
