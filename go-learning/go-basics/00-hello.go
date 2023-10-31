// structures in Go 
package main

import "fmt"

type Person struct {
	firstName string 
	lastName string 
	salary int 
} 

func main() {
	fmt.Println("main function invoked.")

	person := Person {
		firstName: "Sonu",
		lastName : "Singh",
		salary: 10,
	}

	fmt.Println(person) // {Sonu Singh 10}
	fmt.Println(person.firstName) // Sonu

}


// // pointers in Go 
// package main

// import "fmt"

// func main() {
// 	fmt.Println("main function invoked.")

// 	num := 10 // 
// 	poi := &num  // pinter to num 

// 	fmt.Println(num)
// 	fmt.Println(&num)
// 	fmt.Println(poi)
// }


// // // functions in Go

// package main

// import "fmt"

// func main() {

// 	fmt.Println("main function invoked.")
// 	funFunction()
// 	addNums(10)
// 	addNums(10)
// 	addNums(10, 20)
// 	addNums(10, 20, 30)
// }

// func funFunction() {
// 	fmt.Println("fun function invoked.")
// }

// func addNums(num1 int, num2 int) {
// 	fmt.Println(num1 + num2)

// }

// // // type conversion in Go
// // package main

// // import "fmt"

// // func main() {

// // 	salary := 10.25 // float64
// // 	bonus := 10     // int

// // 	fmt.Println(bonus)

// // 	bonus = 20

// // 	fmt.Println(bonus)

// // 	pay1 := salary + float64(bonus)
// // 	pay2 := int(salary) + bonus

// // 	fmt.Println(pay1)
// // 	fmt.Println(pay2)

// // 	const num3 = 30
// // 	fmt.Println(num3)

// // 	num3 = 35

// // }

// // // datatypes in Go
// // package main

// // import "fmt"

// // func main() {

// // 	eid := 101
// // 	firstName := "Sonu"
// // 	salary := 10.25
// // 	isMarried := false

// // 	fmt.Println(eid)
// // 	fmt.Println(firstName)
// // 	fmt.Println(salary)
// // 	fmt.Println(isMarried)

// // }

// // run with
// // go run hello.go

// // package main

// // import "fmt"

// // func main() {

// // 	// variable declaration
// // 	var num int = 10
// // 	fmt.Println(num)

// // 	// variable declaration - shorthand
// // 	num2 := 20
// // 	fmt.Println(num2)

// // 	fmt.Println("Hello world!")

// // }

// // // run with
// // // go run hello.go
