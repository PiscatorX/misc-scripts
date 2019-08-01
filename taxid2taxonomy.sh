#/bin/bash


while IFS=$'\t' read -r -a Taxa_data
do
    species="${Taxa_data[0]}"
    taxa_id="${Taxa_data[1]}"
    taxonomy=`taxgetup  taxon:$taxa_id  -stdout -auto -oformat excel | cut -f 5  | xargs`
    echo -e "$species\t$taxa_id\t|$taxonomy"
    

done  <  $1
