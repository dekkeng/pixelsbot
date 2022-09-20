# Farm Bot for pixels.xyz game
This is a farm bot for pixels.xyz

===========================
# Requirements
===========================
- Installed Python 2.7+
- OS: Windows 10 recommended

===========================
# Configuration
===========================
There are default configurations that suit my screen, but you can adjust to suit your screen.
Adjust values inside config.txt file to suit your screen and run bot smoothly.

===========================
# How to run
===========================
1. Unzip to desired folder.
2. Open Powershell to the folder that you extracted from step 1.
3. Run this command in Powershell: pip install -r requirements.txt
4. Login to pixels game and go to farm that you want to use the bot (farm121 is recommended).
5. capture all images with your screen by check images in sample folder to see what should be captured and replace it with your samples
6. Start the bot by double click to run pixelsbot.py file for normal farm bot,
   fertilize.py for fertilize bot
7. Bot should start working and keep farming for you until it stuck somewhere (hopefully not).

===========================
# Remarks
===========================
- This bot is created very quickly and might have some glitchs or bugs.
- Found bugs or suggestions, feel free to contact me via Discord (dekkeng#9999) or Twitter (@dekkeng).
- If you would like to donate me. You can send ETH, DAI, USDT, USDC to this crypto currency wallet below:
  0xbf20064C795362e7A87F6d21fe3C57Bd99e4a9A5

===========================
# Changelog
===========================
# v 0.0.5
+ Added config file and sample default
+ Added `START_MAP_WALK_DIR` and `START_MAP_WALK_STEP` configs
+ Fixed error when character not found

# v 0.0.4
+ Added fertilize bot to loop harvest, plant, fertilize, refill energy on the same map until run out of fertilize
+ Added sameple images of fertilize, grow1, grow2

# v 0.0.3
+ Added walk to warp feature to find most right warp on the screen and walk toward it

# v 0.0.1
+ Inital project