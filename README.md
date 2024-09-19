# py-notify

A simple python program that notifies the user via Telegram when a command execution is finished. All you need to do is to append the python script to the desired Linux command via a Linux pipe.

Example:
```
$ command | python3 py-notify/main.py
```

However, we need to set up our Telegram bot beforehand. 

## Setup
1. If you do not already have a Telegram bot, you need to set up your own bot via [BotFather](https://t.me/botfather).

2. Now we need to save the bot token and the desired chat id in the [config file](./config.json). 

    - In order to get the chat id for the bot itself, open the following URL in a browser:
        ```
        https://api.telegram.org/bot{our_bot_token}/getUpdates
        ```
    - Look for the message with the text `/start`. In this message, under `chat` we can find our `id`

## Optional: create alias
This repo contains a bash script that automatically creates an alias under `py-notify`. Just execute the following command:

```
./create_alias.sh
```

If you are using `zsh` you need to manually add the following alias to `~/.zshrc`

```
alias $ALIAS_NAME="python3 $MAIN_SCRIPT"
```

After adding the above alias, we need to update the shell with:
```
source ~/.zshrc
```