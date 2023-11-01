package main

import (
    "fmt"
    "time"
)

func main() {
	fmt.Println("Start") 
    go fun1() 
    go fun2() 
    time.Sleep(1 * time.Second)
    fmt.Println("End")
}

func fun1() {
    for i := 0; i <= 10; i++ {
        fmt.Println("fun1:", i)
        time.Sleep(100 * time.Millisecond)
    }
}

func fun2() {
    for i := 11; i <= 20; i++ {
        fmt.Println("fun2:", i)
        time.Sleep(100 * time.Millisecond)
    }
}

