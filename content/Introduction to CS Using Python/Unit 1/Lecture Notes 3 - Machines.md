# 600.1 - Video: Machines

**2 Types of Computers**

- Fixed program computer
	- Handheld calculators
	- Alan Turing's Bombe - designed during WWII for breaking German Enigma encryption
	- Designed for single purpose; solving one type of program

- Stored program computer
	- machine stores and executes instructions
	- walks through, at start-up, the stored executions that the programmer loads

**Basic Machine Architecture of Stored Program Computer**

- Memory
	- Data
	- Mechanical set of steps
- ALU - *Arithmetic Logic Unit*
	- Takes information from memory, often 2 pieces of info
	- Performs primitive operations: *addition, subtraction, division, multiplication, etc*
	- Stores result of operation back into memory
- Control Unit
	- Keeps track of specific operations currently taking place in ALU
	- Consists of a *Program Counter*
		- Counts the steps of a certain program that is loaded into memory in sequence
		- Reads instructions in sequence and adds 1 to counter at every step
		- Tests some predicate for true or false and, depending the result of the test, changes the program counter, accordingly
		- Will stop when the stored program instructs it to do so
		- Points the ALU/computer to the next instruction to execute in the program

**Summary of Stored Program Computer**

- Sequence of instructions loaded into memory
- Built out of simple arithmetic and logic instructions
- Built out of simple tests
- Allows data to moved in and out of memory
- A special program, called an *interpreter* will execute the instructions in sequence
- Flow control, based on the results of the aforementioned tests, will allow program go to different parts of program
- The result of the program will be output or 'printed' for the user

**Basic Primitives**

- Alan Turing showed that anything can be computed with only *6 primitives* - *Eg. A Turing Machine*[^1]
- The operations include: move left, move right, scan, read, write, do nothing
- Modern programming languages come with *abstracted* primitives
- Anything computable in one programming language is computable in another language. However, some languages may offer better abstractions/facilities for performing certain tasks.
	- This property is called *Turing Completeness*[^3]
___

[^1]: [Turing machine - Wikipedia](https://en.wikipedia.org/wiki/Turing_machine)
[^2]: [Turing completeness - Wikipedia](https://en.wikipedia.org/wiki/Turing_completeness)

