#!/bin/bash
#ffmpeg -i octa-export-dnb01-01.wav -ar 44100 octa-export-dnb01-01-44100.wav
python3 main.py '/Users/stephane/Liveact/dnb01/non_master' 'octa-export-dnb01-01-44100.wav' 175 32
