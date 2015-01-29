#!/bin/bash

selection=
until [ "$selection" = "0" ]; do
    echo "
    30C3: Live-Streams (SD-HQ)
    1 - Saal 1 (1hd for HD)
    2 - Saal 2
    3 - Saal G
    4 - Saal 6

    30C3: Live-Streams (SD)
    5 - Saal 1
    6 - Saal 2
    7 - Saal G
    8 - Saal 6

    0 - exit program
"
    echo -n "Enter selection: "
    read selection
    echo ""
    case $selection in
        1 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal1_native_hq ;;
        1hd ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal1_native_hd ;;
        2 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal2_native_hq ;;
        3 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saalg_native_hq ;;
        4 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal6_native_hq ;;
        5 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal1_native_lq ;;
        6 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal2_native_lq ;;
        7 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saalg_native_lq ;;
        8 ) omxplayer rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal6_native_lq ;;
        0 ) exit ;;
        * ) echo "Please enter 1, 2, 3, 4, 5, 6, 7, 8 or 0"
    esac
done
