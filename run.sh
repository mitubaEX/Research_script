# $1 search_birthmark $2 birthmark
cd ./script/frequence_check
go build main.go
cd -

# search
python ./script/search/simple_searcher_kgram.py $1 $2

# frequence_check
for i in 2gram 3gram 4gram 5gram 6gram ; do find ./data/search_result/"$i" -type f | while read file ; do ./script/frequence_check/main "$file" > ./data/frequence_search_result/"$i"/`basename "$file"`;done;done

# parse_search_result
python ./script/parse_search_result/parse_search_result.py $2

# false_positive
# for i in 025 05 075 ; do for l in 2gram 3gram 4gram 5gram 6gram ; do python ./script/false_positive/false_positive.py "$i" "$l" > ./data/false_positive/"$l"/result"$i".csv ;done;done
for i in 025 05 075 ; do python ./script/false_positive/false_positive.py "$i" $2 > ./data/false_positive/$2/result"$i".csv ;done
