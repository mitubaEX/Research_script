package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	var searchTime = ""
	var max_score = 0.0
	var count_075 = 0
	var count_05 = 0
	var count_025 = 0
	var result = []float64{}

	// ファイル読み取り(引数でファイル名受け取り)
	fp, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}
	defer fp.Close()
	scanner := bufio.NewScanner(fp)
	for scanner.Scan() {
		text := scanner.Text()
		if strings.Contains(text, "searchTime") {
			searchTime = text
		} else if strings.Contains(text, ",") {
			split_string := strings.Split(text, ",")
			score, err := strconv.ParseFloat(split_string[1], 64)
			if err != nil {
				// fmt.Println(err)
			}
			max_score = math.Max(score, max_score)
			result = append(result, score)
		}
		// fmt.Println(scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		// panic(err)
		// fmt.Println(err)
	}

	for _, res := range result {
		fmt.Printf("%f %f\n", res, max_score)
		score := float64(res) / float64(max_score)
		fmt.Println(score)
		fmt.Println(res)
		if score >= float64(0.75) {
			count_075 += 1
		}
		if score >= float64(0.5) {
			count_05 += 1
		}
		if score >= float64(0.25) {
			count_025 += 1
		}
	}
	fmt.Println(searchTime)
	fmt.Println(count_075)
	fmt.Println(count_05)
	fmt.Println(count_025)

	// fmt.Println("vim-go")
}
