package main

import (
	"fmt"
	"mercdemo/merc"
)

func main() {
	fmt.Println("main")

	sum := merc.AddNums(10, 20)
	fmt.Println(sum)

	sum2 := merc.SubNums(20, 10)
	fmt.Println((sum2))

}
