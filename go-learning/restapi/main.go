package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
    "github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
    "net/http"
)

type Blog struct {
    ID   int   `gorm:"primary_key" json:"id"`
    Title string `json:"title"`
    Body string `json:"body"`
    UserId int `json:"userId"`
}

func (Blog) TableName() string {
    return "blogs"
}

func main() {
	fmt.Println("main")

	db, err := gorm.Open("postgres", "user=postgres dbname=merc-2023 sslmode=disable password=root")
    if err != nil {
        panic(err)
    }
    defer db.Close()

	db.AutoMigrate(&Blog{})

	router := gin.Default()
	router.GET("/", func (c *gin.Context) {
		fmt.Println("hello")
		c.String(http.StatusOK, "Hello")
	})

	router.GET("/blogs", func (c *gin.Context) {
		fmt.Println("getBlogs")
		var data []Blog
		if err := db.Find(&data).Error; err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve data"})
			return
		}
		c.JSON(http.StatusOK, data)
	})
	
	router.Run("localhost:8090")
}


