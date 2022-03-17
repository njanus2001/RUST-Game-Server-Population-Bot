# Rust Game Server Population Bot
A lightweight discord bot that displays a RUST game server's player count via the bot's status.

# Requirements
1. [RUST](https://store.steampowered.com/app/252490/Rust/) game server using [BattleMetrics](https://www.battlemetrics.com/).
2. [Pterodactyl](https://pterodactyl.io/) game panel.
3. A [Discord](https://discord.com/) server.

# How to use

### Bot Variables
Ensure that the variables at the top of the **bot.py** file are set to your unique values.

### Create a Discord Bot
Create a simple Discord bot using the [Discord Developer Portal](https://discord.com/developers/docs).

### Pterodactyl Server Setup
1. Create a new Pterodactyl server using a **discord.py generic** egg.
2. Set the correct file paths for both the **Bot py file** and **Requirements file** fields in the **Startup** section.
3. Create a folder for the bot files.
4. Upload the bot files into your new folder.

### Start Server
Start your bot's server.

The bot will print "*Bot is now active.*" once successfully started.

A timestamped message will be printed if the bot ever fails to update it's status during any interval.
