# rend.sh <G> <html> <dur> <buildEnd> : 4 parallel chunks then post
G=$1; H=$2; D=$3; B=$4; N=$(python3 -c "print(round($D*60))"); Q=$(( (N+3)/4 ))
export NODE_PATH=$(npm root -g); export SUBB=${SUBB:-1}
for c in 0 1 2 3; do FROM=$((c*Q)) TO=$(((c+1)*Q)) node kit/render.js $G $H $D $B & done; wait
(python3 kit/post.py $G ${G}_out $D > $G/post.log 2>&1 && echo POSTED >> $G/post.log) &
