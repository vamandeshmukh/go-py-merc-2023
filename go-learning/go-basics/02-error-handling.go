package main

import (
	"fmt"
)

func main() {
	fmt.Println("Start")

	friends := []string {"Sonu", "Monu", "Tonu"}

	ind := 1
	if ind < len(friends) {
		fmt.Println(friends[ind])
	}

	fmt.Println("End")
}



// // 02-error-handling.go
// package main

// import (
// 	"fmt"
// 	"errors"
// )

// func main() {
// 	fmt.Println("Start")

// 	output, err := divNums(10, 0)
// 	fmt.Println(output)
// 	if err != nil {
// 		fmt.Println(err)
// }
// 	fmt.Println("End")
// }

// func divNums (a, b int) (int, error) {
// 	if ( b == 0) {
// 		return 0, errors.New("do not divide by 0")
// 	}
// 	return a / b, nil
// }

