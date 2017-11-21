# $1 search_birthmark $2 birthmark
cd ./script/frequence_check
go build main.go
cd -
python ./script/search/simple_searcher_kgram.py $1 $2
sh ./script/frequence_check/script_go.sh
python ./script/parse_search_result/parse_search_result.py $2
