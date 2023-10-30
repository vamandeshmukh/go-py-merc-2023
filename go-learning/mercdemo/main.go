package main

// on module folder on CMD -
// go install
// mercdemo

import (
	"fmt"
	"mercdemo/benz"
	"mercdemo/merc"
)

func main() {
	fmt.Println("main")

	sum := merc.AddNums(10, 20)
	fmt.Println(sum)

	sum2 := merc.SubNums(20, 10)
	fmt.Println((sum2))

	sum3 := benz.DivNums(20, 10)
	fmt.Println((sum3))

	sum4 := benz.MultiNums(10, 20)
	fmt.Println((sum4))

}
