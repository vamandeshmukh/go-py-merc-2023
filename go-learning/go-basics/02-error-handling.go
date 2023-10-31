// 02-error-handling.go
package main

import (
	"fmt"
	"errors"
)

func main() {
	fmt.Println("Start")

	output, err := divNums(10, 0)
	fmt.Println(output)
	if err != nil {
		fmt.Println(err)
}
	fmt.Println("End")
}

func divNums (a, b int) (int, error) {
	if ( b == 0) {
		return 0, errors.New("do not divide by 0")
	}
	return a / b, nil
}

