# Unit 600.1 - Video: Languages

**Creating 'Recipes'**

- A programming language provides a set of primitive operations
- An *expression* is a complex, but legal, combination of primitives in a programming language
- *Expressions* and computations have *values* and meanings in a programming language
- Any legal computation in an expression has a *value* associated with it - it is the meaning of the *expression*
- Every programming language could be thought of consisting:
	- A set of primitives
	- A formal means of combining those primitives into *expressions*
	- A formal means of *abstracting* a complex expression and treating it as a primitive

**Constructs of A Programming Languages**
- Eg: English has *words* as primitives
- Programming languages typically consist of these primitives: numbers, strings, simple operators

**Aspects of a Programming Language**

*Syntax*
- the parsing of a sentence to determine whether a sentence, or *expression*, is legal
- English Eg: "cat dog boy" -> syntactically invalid; no verb // "cat hugs boy" -> syntactically valid; has a subject, object and verb
- Programming language Eg: "hi" 5 -> not syntactically valid; only has two primitive data types, but no operator // 3.2 * 5 -> syntactically valid; has an operator that accepts two pieces of data as input to produce an output

Associated with every syntactically correct expression is meaning - the *semantics*. i.e what does the expression evaluate to?

*Static Semantics*
- Tells us which syntactically valid strings actually have a meaning
	- English Eg: "I are hungry" -> consists of a subject and verb; syntactically correct, however, carries no semantic meaning
	- Programming language example: 3 + "hello"  -> static semantic error; consists of two inputs and an operator, but means nothing because, semantically, the language cannot perform the operation on a number and a string.

*Semantics* is the meaning associated with a syntactically correct string of symbols with no *static semantic* errors.

Syntactically and semantically correct expressions in English can have many meanings:
- "Flying planes can be dangerous"
- "This reading lamp hasn't uttered a word since I bought it."

Programming languages have only one meaning but may not be what the programmer intended.

Examples of issues when a program is both syntactically and statically semantically correct, but behaves differently to what is expected:
- Program might crash
- Program will run indefinitely
- The results of the computation will be different to what is expected, or may not be accurate.

___
