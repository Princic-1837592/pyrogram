# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import pyrogram
from pyrogram.api import functions
from ...ext import BaseClient


class CreateSupergroup(BaseClient):
    def create_supergroup(
        self,
        title: str,
        description: str = ""
    ) -> "pyrogram.Chat":
        """Create a new supergroup.

        .. note::

            If you want to create a new basic group, use :meth:`~pyrogram.Client.create_group` instead.

        Parameters:
            title (``str``):
                The supergroup title.

            description (``str``, *optional*):
                The supergroup description.

        Returns:
            :obj:`Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                app.create_supergroup("Supergroup Title", "Supergroup Description")
        """
        r = self.send(
            functions.channels.CreateChannel(
                title=title,
                about=description,
                megagroup=True
            )
        )

        return pyrogram.Chat._parse_chat(self, r.chats[0])
