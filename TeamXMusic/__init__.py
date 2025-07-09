from TeamXMusic.core.bot import Teamy
from TeamXMusic.core.dir import dirr
from TeamXMusic.core.git import git
from TeamXMusic.core.userbot import Userbot
from TeamXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Teamy()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
