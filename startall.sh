#!/bin/bash
# Author : thejackal

# Let the desktop load for a few seconds before running
sleep 5

# Kill all current conky processes.
killall conky
#> /dev/null &

#https://github.com/zagortenay333/conky_themes


# Starting all  conky widgets.
conky -c ~/.config/conky/conky_thejackal_L.conf &
conky -c ~/.config/conky/conky_thejackal_M.conf &
##conky -c ~/.config/conky/conky_thejackal_Calendario.conf &
conky -c ~/.config/conky/conky_thejackal_R.conf &