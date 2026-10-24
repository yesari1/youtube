# queue.sh "G01 g01.html 16.1 11" "G02 ..." : render each in turn
for job in "$@"; do bash rend.sh $job > $(echo $job|cut -d' ' -f1)/render.log 2>&1; done; echo QUEUEDONE
