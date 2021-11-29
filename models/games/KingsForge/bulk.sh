#!zsh

for FILE in {Cards,Trays,Other}/*; do
  NAME=${${FILE#*/}%.*}
  # NAME=$(basename $FILE)
  echo "Starting with file $FILE"
  echo "basenmae: $(basename $FILE)"
  echo "Slicing $NAME"
  echo "---------------------------"
  /Applications/Original\ Prusa\ Drivers/PrusaSlicer.app/Contents/MacOS/PrusaSlicer \
    --printer-technology FFF \
    --center 125,105 \
    --export-gcode --loglevel 0 \
    --load "PrusaSlicer_config_bundle.ini" \
    --output output/$NAME.gcode \
    $FILE
done
