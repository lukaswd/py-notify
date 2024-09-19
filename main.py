import requests
import logging
import sys
import argparse
import json

from pathlib import Path

file_dir = Path(__file__).parent.resolve()

# Set up basic logging to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger()

def send_message(token, chat_id, message):
    logging.info(f"Sending message: {message} to chat_id: {chat_id} with bot token: {token}")

    message = "Py-Notify: " + message

    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    else:
        logger.error(f"Sending Message failed with status code {r.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python notification via telegram chat\n Usage: command | py-notify")
    parser.add_argument("-m", "--message", dest="message", help="Send a custom message to the chat instead of the default message")
    parser.add_argument("-q", "--quiet", dest="quiet", action="store_true", help="Do not print the outptu to the console")
    parser.add_argument("-c", "--config", dest="config", help="Path to the config file (default: config.json)")

    args = parser.parse_args()

    if args.config:
        config_file = Path(args.config)
        if not config_file.is_file():
            logger.error(f"Config file {config_file.as_posix()} does not exist.")
            sys.exit(1)
    else:
        config_file = Path.joinpath(file_dir, "config.json")

    with open(config_file, "r") as f:
        config = json.load(f)

    if not "bot_token" in config or config["bot_token"] is None:
        logger.error("No bot token found in config file. Please add your bot token to the config file and try again.")
        sys.exit(1) 
    if not "chat_id" in config or config["chat_id"] is None:
        logger.error("No chat id found in config file. Please add your chat id to the config file and try again.")
        sys.exit(1)

    bot_token = config["bot_token"]
    chat_id = config["chat_id"]

    try:
        data = sys.stdin.read()
    except Exception as e:
        logger.error(f"Error reading input: {e}")
        sys.exit(1)

    if not args.quiet:
        print(data)

    if args.message:
        send_message(bot_token, chat_id, args.message)
    elif args.quiet:
        send_message(bot_token, chat_id, "Finished running command")
    else:
        send_message(bot_token, chat_id, f"Finished running command with output:\n{data}")
    