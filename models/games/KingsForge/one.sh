#!zsh

#for FILE in {Cards,Trays}/*; do
  NAME=${${1#*/}%.*}
  # NAME=$(basename $FILE)
  echo "Starting with file $1"
  echo "basenmae: $(basename $1)"
  echo "Slicing $NAME"
  echo "---------------------------"
  /Applications/Original\ Prusa\ Drivers/PrusaSlicer.app/Contents/MacOS/PrusaSlicer \
    --printer-technology FFF \
    --center 125,105 \
    --export-gcode --loglevel 0 \
    --load "Original Prusa i3 MK3S - Copy.ini" \
    --load "Prusament PLA - Copy.ini" \
    --load "0.30mm DRAFT @MK3 - Slow 1st layer.ini" \
    --output output/$NAME.gcode \
    $FILE
#done
