# The Menga Programming Language
is a json-syntax based programming language, compiled using the jcc compiler.

_Yes, this language was created as a joke._
* [Tools](#tools)
* [Installation](#installation)
* [Documentation](#documentation)
* [Examples](#examples)

# Tools

- **jcc**: Menga comes with jcc, the json-code-compiler.

# Installation
### jcc
Clone the repository, then install via makefile:

```
git clone https://github.com/menga-team/menga-lang
cd menga-lang
```
```
sudo make install
```

To uninstall menga-lang tools, run
```
sudo make uninstall
```

### System requirements

jcc works on unix systems, and therefore not on Windows.
Windows support will be added eventually.

# Manual

### jcc

Code can be compiled by providing the source file and an executable name:

```
jcc yourcode.json executable_name
```


# Documentation

Menga-code is written in the json-sytax. When "compiled" with jcc, it is interpreted to C++, which then is compiled to an executable. Therefore, Menga is quite similar to C++, but less extensive. In case you were wondering: Yes, that means creating the Language was a piece of cake, since not a single line of Machine Code, Assembly or even C was required. The jcc interpreter consists of a python script to interpret Menga to C++ and some bash scripts to make things easier for the user.


## Declarations
Possible values: `variable`, `array`, `function`, `object`

### variable

```json
{"declare": "variable", "type": "int", "name": "kira_yoshikage", "value": 33}
```
`type`: object type. One of Menga's inbuilt objects or a custom object declared with `object`

`name`: name to reference the variable later

`value`: optional, the variable's value

### array

```json
{"declare" : "array", "type" : "string", "name" : "food", "value": ["sandwich", "apple", "banana"]}
```
Identical to variables, but the value is given as an array.

### function

```json
{"declare": "function",
    "name":"print",
    "return": "void",
    "parameters": [{"number": "int"}],
    "instructions": [{"print": [{"string": "Your value is: "}, {"variable": "number"}]}]
}
```
`return`: object type of return value. `void` for methods, one of Menga's inbuilt objects or a custom object declared with `object`

`parameters`: array of parameters, elements 

### object

```json
{"declare": "object",
    "name": "girlfriend",
    "private": [
        {"declare": "variable", "type": "bool", "name": "exists", "value": false}
    ],
    "public": [
        {"declare": "function",
            "name": "set_existance",
            "return": "void",
            "parameters": [{"existance": "bool"}]
            "instructions": [{"set": "exists", "variable": "existance"}]
        }
    ]
}
```
`private`: array containing all private declarations

`public`: array containing all public declarations

## Other Instructions

### call
```json
{"call": "eat", "parameters": [{"string": "banana"}]}
```

### print
```json
{"print": [{"string": "Hello, my name is "}, {"variable": "name"}]}
```
## Builtins

### objects
`string`, `int`, `bool`

### functions
`randseed`: sets random seed to current time

`randrange`: parameters: `int min`, `int max`. Returns random integer in given range.


# Examples

### Hello World!
```json
{"declare": "function",
    "name":"main",
    "return": "int",
    "parameters": [],
    "instructions": [
      {"print": [{"string": "Hello World!"}]}
    ]
  }
```
