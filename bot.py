#!/usr/bin/env python3

import discord
import requests
import asyncio
from datetime import datetime

# CHANGE THESE!
REFRESH_RATE = 5 # Discord bot status refresh rate (seconds)

SERVER_ID = '' # BattleMetrics server ID
DC_TOKEN = '' # Discord bot token
BM_TOKEN = '' # BattleMetrics OAuth 2.0 Bearer token
##############

HEADERS = {"Authorization": f"Bearer {BM_TOKEN}"}
URL = f'https://api.battlemetrics.com/servers/{SERVER_ID}'


async def update_status():
    """ Updates discord bot status. """
    await client.wait_until_ready()
    print('Bot is now active.')
    
    while True:
        server_info = get_server_info()

        if len(server_info) == 4:
            try:
                if server_info[3] == 'online' and server_info[2] == 0:
                    await client.change_presence(activity=discord.Game(name=f'{server_info[0]}/{server_info[1]}'))
                elif server_info[3] == 'online' and server_info[2] > 0:
                        await client.change_presence(activity=discord.Game(name=f'{server_info[0]}/{server_info[1]} ({server_info[2]} Queued)'))
                else:
                    await client.change_presence(activity=discord.Game(name=f'Offline/Restarting'))
                
            except Exception:
                now = datetime.now()
                time = now.strftime("%H:%M:%S")
                print(f'{time} - Failed to update bot')
                

        await asyncio.sleep(REFRESH_RATE)


def get_server_info():
    """ Retrieves certain server information from BattleMetrics API. """
    try:
        response = requests.get(URL, headers=HEADERS)

        server_info = response.json()

        info = []

        info.append(server_info['data']['attributes']['players'])
        info.append(server_info['data']['attributes']['maxPlayers'])
        info.append(server_info['data']['attributes']
                    ['details']['rust_queued_players'])
        info.append(server_info['data']['attributes']['status'])
        
    except Exception as e:
        print(e)
        return []

    return info


if __name__ == "__main__":
    """ Main. """
    client = discord.Client()
    client.loop.create_task(update_status())
    client.run(DC_TOKEN)
