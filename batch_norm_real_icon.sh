#/bin/sh

set -x

input_prefix="icons_real/"
output_prefix="real_icons_styled_"
extension="png"
noused_style_list="
woman
shipwreck
minwha_2
water_4
gc
pattern_1
sumookwha_1
leaf_pattern_1
water_3
"
chosen_style_list="
seated-nude
the_scream
woman-with-hat-matisse
starry-night
kandinsky
s5_wall
"

for style in $chosen_style_list
do
    for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    do
        python norm_icon_run.py ${input_prefix}${i}.$extension images/${style}.jpg ${output_prefix}result_${style}${i}.$extension || exit $i
    done
    # gsutil mv ${output_prefix}result_*.$extension gs://q1-tensorflow
done

sudo poweroff
# gcloud compute instances stop instance-2 --zone=us-east1-b
