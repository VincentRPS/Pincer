from ..core.dispatch import GatewayDispatch as GatewayDispatch
from ..objects.events.thread import ThreadListSyncEvent as ThreadListSyncEvent
from ..utils.conversion import construct_client_dict as construct_client_dict

async def thread_list_sync(self, payload: GatewayDispatch): ...
def export(): ...
