from ..core.dispatch import GatewayDispatch as GatewayDispatch
from ..objects.events.integration import IntegrationCreateEvent as IntegrationCreateEvent
from ..utils.conversion import construct_client_dict as construct_client_dict
from ..utils.types import Coro as Coro

async def integration_create_middleware(self, payload: GatewayDispatch): ...
def export() -> Coro: ...
