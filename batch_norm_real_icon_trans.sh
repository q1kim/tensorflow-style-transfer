#/bin/sh

set -x

input_prefix="icons_real/"
output_prefix="real_icons_styled_"
extension="png"

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14
do
    python norm_icon_run_trans.py ${input_prefix}${i}.$extension images/${style}.jpg ${output_prefix}result_${style}${i}.$extension || exit $i
done

# gsutil mv ${output_prefix}result_*.$extension gs://q1-tensorflow
# sudo poweroff
# gcloud compute instances stop instance-2 --zone=us-east1-b
