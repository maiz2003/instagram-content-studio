#!/bin/bash
# Brand-guardian render checks for one Reel: size/fps, loudness, peak, silent gaps, and a 12-frame contact sheet.
# Usage: FFMPEG=... bash qa.sh <reel.mp4> <sheet.png>
f=$1; sheet=$2
d=$($FFMPEG -i "$f" 2>&1 | grep -o "Duration: [0-9:.]*" | cut -d' ' -f2)
v=$($FFMPEG -i "$f" 2>&1 | grep -o "Video: .*" | grep -oE "[0-9]{3,4}x[0-9]{3,4}|[0-9.]+ fps" | tr '\n' ' ')
lufs=$($FFMPEG -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -A20 "Summary" | grep -E "I:|Peak:" | awk '{print $2}' | tr '\n' ' ')
gaps=$($FFMPEG -hide_banner -nostats -i "$f" -af silencedetect=n=-45dB:d=0.4 -f null - 2>&1 | grep -c "silence_start")
echo "$(basename $f) | $d | $v | LUFS/peak: $lufs | silent gaps: $gaps"
$FFMPEG -v error -y -i "$f" -vf "fps=12/$(echo $d | awk -F: '{print $3+0}'),scale=240:427,tile=6x2:padding=3" -frames:v 1 "$sheet"
