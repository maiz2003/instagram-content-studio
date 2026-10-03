#!/bin/bash
# Render week-3 Reels. Run from the repo root: bash outputs/lock-in/2026-10-week3/render.sh [slug ...]
# Needs NODE_PATH (global Playwright) and FFMPEG set; see agents/video-producer.md.
set -u
cd "$(dirname "$0")/../../.."
DIR=outputs/lock-in/2026-10-week3/reels
SLUGS=${@:-$(ls $DIR/*.json | xargs -n1 basename | sed 's/\.json$//')}
for s in $SLUGS; do
  echo "render $s"
  node scripts/render/reel.js $DIR/$s.json $DIR/$s.mp4 > $DIR/$s.log 2>&1 && echo "ok $s" || echo "FAIL $s"
done
