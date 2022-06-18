# A Totally Legit Working Discord Bot
This bot is meant to be a work in progress and is currently being developed for an unofficial intern Discord server for Oracle. Contributions are welcome through creating PRs.

# Installation
Ensure that you have Python 3 installed, and follow these [instructions](https://discordpy.readthedocs.io/en/stable/discord.html) to create a bot account on Discord.
Afterwards, install the Discord API [here](https://discordpy.readthedocs.io/en/stable/intro.html#installing).
Clone this repo with:
```
git clone https://github.com/jhern603/TotallyLegitDiscordBot.git
```
Prior to starting the bot, create a `.conf` file at the root of the project. The file should follow this format:
```
[MYBOT]
token=<The bot user token>
oauth-client-public=<used for oauth> [UNUSED]
oauth-client-secret=<used for oauth> [UNUSED]
app-id=<the Discord application ID for HTTP requests> [UNUSED]
public-key=<public app id> [UNUSED]
```
Start the bot with:
```
python3 main.py
```
Edit the command prefix, bot log channel, and other bot settings via `settings.conf`