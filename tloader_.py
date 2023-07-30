import logging, re, asyncio

from telethon.tl.types import MessageEntityTextUrl
from hikkatl.types import Message
from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class secret_thing(loader.Module):
    
    def __init__(self):
        self.iris = 5443619563
    
    async def client_ready(self, client, db):
        self._me = await client.get_me()
        val = False
        bag = {'iris': 0, 'gold': 0, 'id': None}
        while True:
            if val:
                break
            temp = await self._client.send_message(self.iris, 'мешок')
            await asyncio.sleep(4)
            for msg in await self._client.get_messages(self.iris, limit = 1):
                parts = msg.text.splitlines()
                for msdel in [msg, temp]:
                    await msdel.delete()
                
                if '💰 В мешке' in msg.text[:9] and len(msg.text.splitlines()) > 3 and msg.entities:
                    if 'ириски' in msg.raw_text:
                        iriski = int(parts[1].split('🍬')[1].split('ириски')[0].strip(' '))
                    else:
                        iriski = int(parts[1].split('🍬')[1].split('ирисок')[0].strip(' '))
                    gold = int(parts[1].split('🌕')[1].split('ирис-голд')[0].strip(' '))
                    for url_entity, inner_text in msg.get_entities_text(MessageEntityTextUrl)[:1]:
                        id = url_entity.url.replace('tg://openmessage?user_id=', '').replace('https://t.me', '')
                        name = inner_text
                    if id == str(self._me.id):
                        bag['iris'] = iriski
                        bag['gold'] = gold
                        bag['id'] = id
                        val = True
                        break
        if bag.get('id'):
            print(f'В мешке {name}:{id} - {iriski} ирисок, {gold} голд')
            

