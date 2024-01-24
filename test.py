from plover.config import Config
from plover.oslayer.config import CONFIG_FILE
from plover.registry import registry

config = Config(path=CONFIG_FILE)
config.load()
registry.update()
for p in registry.list_plugins('system'):
	print(dir(p), p.name)

from plover.system import NUMBERS

print(NUMBERS)
