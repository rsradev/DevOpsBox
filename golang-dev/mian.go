package main

import "fmt"

/* *
 *Simple Date Types in Go
 *	Strings
 *	Numbers
 *	Booleans
 *	Errors
 *
 *	Strings:
 *	"this is a interpeted string"
 *	`this is a row string`
 *
 *	Numbers:
 *	Integers
 *	UInt
 *	Float(32/64)
 *	Complex(64/128)
 *
 *	Bool(True/False)
 *
 *	Error(interface)
 * */

// be clear than be cleaver

func main() {

	// //Tree(4) way to declare
	var myName1 string
	var myName2 string = "Radi"

	var myName3 = "Ivan"
	myName4 := "Petkan"

	fmt.Println(myName1)
	fmt.Println(myName2)
	fmt.Println(myName3)
	fmt.Println(myName4)

	var i int = 42
	var f float32

	f = float32(i)

	fmt.Printf("The answer of the everithing is %v\n", f)

	//f = i //error

}
