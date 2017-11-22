# $1 search_birthmark $2 birthmark $3 obfuscation

# preservasion_check
python simple_searcher_obfu_args.py $1 $2 $3

mkdir ./data/frequence_search_result/$3/$2

# frequence_check
find ./data/search_result/"$3"/"$2" -type f | while read file ; do ./script/frequence_check/main "$file" > ./data/frequence_search_result/"$3"/"$2"/`basename "$file"`;done

# parse_search_result
python ./script/preservation/parse_search_result.py $2 $3
