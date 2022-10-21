# Farm Bot for pixels.xyz game
This is a farm bot for pixels.xyz

# Requirements
- Installed Python 2.7+ (https://www.python.org/downloads/)
- OS: Windows 10 recommended

# How to run
1. Install Python if you don't already installed.
2. Clone the repository to a folder on your PC.
3. Open Powershell and go to the folder that you extracted from step 2
4. Run this command in Powershell to install required libraries
```bash
pip install -r requirements.txt
```
5. Copy config.txt.default to config.txt file
6. Copy sample.default to sample folder
7. Captured your Pixels game screen and crop it just like sample images on each one (avatar.png will use your avatar with least background).
8. Start the bot by double click at pixelsbot.py or use command python pixelsbot.py in Powershell (You need to open the game at maximized on this step).
9. If it not doing right, you need to adjust configurations in config.txt to fir your screen. (You need to change the values and try few times until it works) This should be one time work.
10. If you want to stop you just open something to hide the game screen and close your running script window.

# Configuration
There are default configurations that suit my screen, but you can adjust to suit your screen.
Adjust values inside config.txt file to suit your screen and run bot smoothly.

| Name | Description | Type | Default | Options |
| --- | --- | --- | --- | --- |
| PLANT_TYPE | Which plant to use | Option | carrot | carrot, gold |
| START_MAP_WALK_DIR | To move when start the new map in which direction | Option | down | down, up, left, right |
| START_MAP_WALK_STEP | How many seconds will you walk at the start of the new map | Second | 0.1 |  |
| WARP_NEAR_DECISION | How many screen pixels to decide that you are near the warp enough to be able to go through it | Pixel | 150 |  |
| WARP_NEAR_STEP | How many seconds for each walk try to go to the warp | Second | 0.3 |  |
| WARP_NEAR_TRY_LIMIT | Maximum times to try to go to warp | Count | 100 |  |
| EMPTY_CONFIDENCE | Percentage confidence to find matching empty.png image on screen | Percentage | 0.6 |  |
| GROW1_CONFIDENCE | Percentage confidence to find matching grow1.png image on screen | Percentage | 0.8 |  |
| GROW2_CONFIDENCE | Percentage confidence to find matching grow2.png image on screen | Percentage | 0.8 |  |
| FULL_CONFIDENCE | Percentage confidence to find matching full.png image on screen | Percentage | 0.75 |  |
| ROTTEN_CONFIDENCE | Percentage confidence to find matching rotten.png image on screen | Percentage | 0.8 |  |
| ROTTEN2_CONFIDENCE | Percentage confidence to find matching rotten2.png image on screen | Percentage | 0.9 |  |
| FERTILIZE_CONFIDENCE | Percentage confidence to find matching fertilize.png image on screen | Percentage | 0.9 |  |
| WARP_CONFIDENCE | Percentage confidence to find matching warp.png image on screen | Percentage | 0.7 |  |
| AVATAR_CONFIDENCE | Percentage confidence to find matching avatar.png image on screen | Percentage | 0.9 |  |
| AVATAR2_CONFIDENCE | Percentage confidence to find matching avatar2.png image on screen | Percentage | 0.9 |  |
| REFILL_AMOUNT_PER_MAP | How many times to refill energy on each map | Count | 10 |  |
| WAIT_DURATION_AFTER_WARP | How many second to wait after warp | Second | 10 |  |
| RANDOM_CLICK_SIZE | To prevent bot detection it will slightly random click position | Pixel | 5 |  |

# Remarks
- This bot is created very quickly and might have some glitchs or bugs.
- If you would like to donate me that will be really appreciated. You can send ETH, DAI, USDT, USDC to this crypto currency wallet below:
  0xbf20064C795362e7A87F6d21fe3C57Bd99e4a9A5

# Changelog
## v 0.0.10
+ Update support new version
+ Update avatar locate instead of name
+ Added avatar.png sample image
+ Added avatar2.png sample image
+ Added `AVATAR_CONFIDENCE` and `AVATAR2_CONFIDENCE` configs

## v 0.0.9
+ Added plant type gold
+ Added `PLANT_TYPE` and `ROTTEN2_CONFIDENCE` configs

## v 0.0.8
+ Added slight random click feature
+ Added `RANDOM_CLICK_SIZE` configs

## v 0.0.7
+ Added rotten.png sample image
+ Added clean rotten out when harvest

## v 0.0.6
+ Added `WAIT_DURATION_AFTER_WARP` configs

## v 0.0.5
+ Added config file and sample default
+ Added `START_MAP_WALK_DIR` and `START_MAP_WALK_STEP` configs
+ Fixed error when character not found

## v 0.0.4
+ Added fertilize bot to loop harvest, plant, fertilize, refill energy on the same map until run out of fertilize
+ Added sameple images of fertilize, grow1, grow2

## v 0.0.3
+ Added walk to warp feature to find most right warp on the screen and walk toward it

## v 0.0.1
+ Inital project
