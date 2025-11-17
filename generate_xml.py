
from channels.rewind import RewindChannel
from channels.aftermath import AftermathChannel

channels = [RewindChannel(), AftermathChannel()]

for channel in channels:
    channel.handle_conversion()


