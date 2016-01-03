# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/DigitalRevCom
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------
# plugintools.py courtesy of tvalacarta@gmail.com,
# more info at http://www.mimediacenter.info/plugintools 
#
# DigitalRevTV by misty 2016
#------------------------------------------------------------

import os
import sys
import xbmc,xbmcaddon
from addon.common.addon import Addon
import plugintools

addonID = 'plugin.video.DigitalRevTV'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
fan_art = local.getAddonInfo('fanart')


# Put channel between quotes: YOUTUBE_CHANNEL_ID = ""
YOUTUBE_CHANNEL_ID = "DigitalRevCom"

# Entry point
def run():
    plugintools.log("DigitalRevTV.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("DigitalRevTV.main_list "+repr(params))

    plugintools.add_item( 
        #action="digrev_latest", 
        title="Digital[COLOR red]Rev[/COLOR] TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        fanart=fan_art,
        folder=True )

run()