import asyncio

from .abstractentity import AbstractEntity
from .utils.wrap_tools import _make_repr

class AbstractUser(AbstractEntity):
    def __init__(self, **options):
        super().__init__(**options)
        self.options = options
    
    def __repr__(self):
        info = {
            'name': repr(self.name),
            'id': self.id,
            'account_id': self.account_id
        }
        return _make_repr(self, info)
        
    @property
    def name(self):
        return self.options.get('name')
    
    @property
    def account_id(self):
        return self.options.get('account_id')
    
    async def to_user(self):
        """|coro|

        Convert ``self`` to :class:`.User` object.

        Returns
        -------
        :class:`.User`
            An user object corresponding to the abstract one.
        """
        from .client import Client
        return await Client().get_user(self.account_id)
