import sys
import logging
import importlib
from pathlib import Path
from pyrogram import Client

import logzero

logger = logzero.logger

def load_plugins(plugin_name):
    path = Path(f"main/plugins/{plugin_name}.py")
    name = "main.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["main.plugins." + plugin_name] = load
    print("main has Imported " + plugin_name)

async def isPremium(client:Client ) -> bool:
    my_info = await client.get_me()
    return my_info.is_premium



