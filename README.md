# Amtbot

Python bot for 64-bit Pi OS using Telegram to notify you about bookable appointments to register an apartment with all government offices in Berlin.

## Set up

This program is designed to run on Pi OS 64 but **it can also run on regular Linux distributions** or all other operating systems able to install the required dependencies.

### Prerequisites

1. Raspberry Pi with a **64-bit** architecture and [Pi OS 64-bit](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit) installed (The bot needs a desktop, so **don't use the Lite version!**)
2. A Telegram bot and it's **bot token** ([How do I create a Telegram bot and receive the bot token](https://core.telegram.org/bots#6-botfather))

### Retrieve chat id

In case you have already set up your bot and you know the id of your chat with the bot, you can skip this step. Otherwise follow these steps:

1. Make sure, your bot is set up correctly
2. Add your bot to a group or directly start a chat with your bot **from your phone** (somehow the next step sometimes does not work from the desktop client)

**Single chat**

1. In Telegram search for "@RawDataBot"
2. Start a chat with "Telegram Bot Raw"
3. The bot will return a message containing your **chat id**

**Group chat**

1. Add your bot to a group
2. Make your bot an admin of the group
3. Open the [web version](https://web.telegram.org) of Telegram **in your browser**
4. Open the group chat
5. Check out the URL. The digits behind "g" are the digits of your chat id
6. **Add a minus** in front of the digits in order to get your complete chat id (e.g. `-45864925`)

---

## How to run

Make sure that you have finished the setup listed above. Clone the repository or download only `bot.py`.

### Install dependencies

1. Install python3 and it's corresponding pip version
2. Install selenium: `pip install selenium`
3. Install telepot: `pip install telepot`
4. Install chromium-chromedriver: `sudo apt install chromium-chromedriver`

The last step should automatically install the required Chrome or Chromium version if it is not already installed.

### Insert values

Open `bot.py` and fill in all variables after `# enter your values`

1. Enter your Telegram bot token in `BOT_TOKEN`
2. Enter your Telegram chat id in `CHAT_ID`
3. Enter your month of moving in **german and uppercase** in `MOVING_MONTH`
4. Enter your year of moving in `MOVING_YEAR`
5. Enter your day of moving in `MOVING_DAY`

### Execute

Navigate inside the folder that `bot.py` resides in and run `python bot.py`.

The bot now runs and checks for available appointments every minute. You can now leave the Raspberry Pi alone. The bot will notify you on Telegram in case it crashes.

---

## Shortcomings

This script was hacked together quite quickly. Feel free to modify the script to your needs.

### Service limits

The bot is written to only look for appointments for registering an appartment. This can be easily switched, by changing the `URL` constant but this is not tested.

### Month limits

The bot does not navigate through the months and years on the page. It expects the month to be visible when loading. This means, that it can only check the current and the next month for available appointments. (The Amt only issues appointments 2 months in advance anyways).

In case you want to see months ahead, you can use the code from line `38 - 40` to click on the "next" button on the page:

```
next_href = driver.find_element(by=By.CLASS_NAME, value="next")
next_link = next_href.find_element(by=By.TAG_NAME, value="a")
next_link.click()
```

### Date limits

The bot only checks for available appointments after the date of your move but only **inside the same month** (because it is a little stupid). This means that you won't have problems with the bot, if your date of moving is before the 14th but afterwards it will not work properly.

**Example 1:** You move April 1st. The bot will check April 2nd - April 30th for available appointments. The bot does it's job okay (only 14 days after the move should actually be checked in order to get the appointment in time)

**Example 2:** You move April 30th. The bot will check 0 dates as it is the last day in the month. The bot does not work at all.

**Example 3:** You move April 15th. The bot will check April 16th - April 30th for available appointments. The bot does it's job perfectly.

You would need to implement your own fix for this in case you move on a date that is not working perfectly for you.
