{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    ":opt no-lint"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Recursion and Folds"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Outline\n",
    "\n",
    "- Why Recursion?\n",
    "- Thinking Recursively\n",
    "    - `sum` and `product`\n",
    "- Steps to create your own recursive function\n",
    "- Examples of recursion\n",
    "    - `and`, `length`, `reverse`, `drop`, `take`, `map`, `filter`\n",
    "- Extracting the `foldr` pattern\n",
    "- The `foldl` function\n",
    "- The `foldl'` function\n",
    "- When to use `foldr`, `foldl`, and `foldl'`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Why Recursion?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "One of the basic functionalities necessary in any programming language is repetition. For example:\n",
    "\n",
    "- You have a list of objects and want to do something to all of them. One by one.\n",
    "- You want to do some calculations 5 times with different values.\n",
    "- Etc."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "In imperative programming languages, these repetitive tasks are dealt with using iterative loops. For example, in JavaScript, you can have:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```javascript\n",
    "for (i = 0; i < 5; i = i + 1) {\n",
    "    // Do something\n",
    "}\n",
    "\n",
    "let i = 0;\n",
    "while (i < 5) {\n",
    "  // Do something\n",
    "  i = i + 1;\n",
    "}\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "But, if we tried to create something like this in Haskell, we'd have a big problem. And that's the variable `i`.\n",
    "\n",
    "As we covered in lesson one, Haskell is a purely functional language. But these two code blocks rely on changing `i` on each iteration. That means they have the side effect of updating a global state as the program progresses."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, in Haskell, we do not have these built-in looping functions. Instead, we have recursion!\n",
    "\n",
    "And how is recursion better than looping, you say? Here're a few reasons:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Reasons why recursion is useful:\n",
    "- Everything you can do with loops, you can do it using recursion. And on top of that, there are even programs that you can recursively define that cannot be written using `for` loops.\n",
    "- Many (if not most) functions can naturally be defined using recursion. This means that the way you abstractly think about the function and the way you write it using recursion is highly similar.\n",
    "- Some functions are more clear and more concise if defined using recursion.\n",
    "- You can use induction to do mathematical reasoning and prove properties of functions defined using recursion. (More advanced, but incredibly powerful.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now that you know you're about to learn a pretty powerful concept, let's dive in!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Thinking Recursively"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Recursion occurs when a thing is defined in terms of itself. So a recursive function is one that it's defined in terms of itself."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "That's it. The concept is really simple. The implementation is what gives most of the trouble. So, we're going to start by defining a function using both a `for` loop (using Python) and recursion (using Haskell) to highlight the difference in the way of thinking about the problem."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Say we want to calculate the sum of a list of numbers.\n",
    "\n",
    "Both Python and Haskell have the function `sum` that already does that. But this time, we're going to create it from scratch. In imperative languages, you would write something like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```python\n",
    "def sum(list):\n",
    "    total = 0\n",
    "    for i in list:\n",
    "        total = total + i\n",
    "    return total\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Here, you're describing step by step what the program should do:\n",
    "\n",
    "1. We create a function named `sum` that takes a `list`.\n",
    "2. Then, we create a variable called `total` with an initial value of `0`.\n",
    "3. Then, for each element in the list, we take `total`, add the element to it, and override the assignment to `total` with the new value.\n",
    "5. After the loop finishes, the function returns the `total` variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see, in imperative languages, we use a sequence of statements to determine HOW to reach a goal. In this case, the sum of the elements in the list. \n",
    "\n",
    "To easily write recursive functions, you have to get rid of that way of thinking and embrace declarative programming. Where you declare what things ARE instead of how to obtain them step by step."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, let's define the same function in Haskell."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As always, the first thing we need to do is to write the type signature:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "sum :: [Int] -> Int\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, we know it takes a list of integers and returns an integer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, based on what the function IS: One that takes a list of numbers and returns its sum, the next step is to look for edge cases.\n",
    "\n",
    "We take a list as input. What happens if the list is empty, for example? Well, in that case, we know that the sum of an empty list IS `0`. So, we can start by defining that:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "sum :: [Int] -> Int\n",
    "sum [] = 0\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, besides that, there's the case when there are elements inside the list:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "sum :: [Int] -> Int\n",
    "sum [] = 0\n",
    "sum (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If we think about what the function `sum` IS on the second definition, it is a function that takes a non-empty list of `Int`s and adds them up. Which is the same as adding `x` (the first element) to the result of adding all the `Int`s in `xs`. So we can do something like:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "sum :: [Int] -> Int\n",
    "sum [] = 0\n",
    "sum (x:xs) = x + ...\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And now, we need to find the sum of all the elements in `xs`. But wait a minute... we already have a function to do that! it's the same we're defining right now! So we can just use it!:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "sum :: [Int] -> Int\n",
    "sum [] = 0\n",
    "sum (x:xs) = x + sum xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And there you go! We implemented our first recursive function! Why? Because we defined `sum` using itself!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Let's see what happens when we use this function. For example, let's calculate the sum of a list that contains all the integers from `1` to `5`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "sum [1,2,3,4,5] = 1 + sum [2,3,4,5]\n",
    "                = 1 + 2 + sum [3,4,5]\n",
    "                = 1 + 2 + 3 + sum [4,5]\n",
    "                = 1 + 2 + 3 + 4 + sum [5]\n",
    "                = 1 + 2 + 3 + 4 + 5 + sum []\n",
    "                = 1 + 2 + 3 + 4 + 5 + 0\n",
    "                = 15\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And that's how Haskell evaluates our function.\n",
    "\n",
    "Notice that the base case is the one that allows us to stop the recursion and have a result. If we define the recursive function without a base case, it'll crash or run forever."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    },
    "tags": [
     "elim?"
    ]
   },
   "source": [
    "So, in a few words:\n",
    "\n",
    "With loops, you change context with a mutating accumulator that wraps the steps to determine HOW to reach the goal.\n",
    "\n",
    "With recursion, you wrap the function with itself, which creates a new context with the desired mutation. And that function, in turn, calls itself again, setting up its own context and so on and so forth."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, even though this was a complete walkthrough of how to create the `sum` recursive function, the reasoning may be a bit too specific to apply to other functions. \n",
    "\n",
    "To make it easy for you to create your own recursive functions, we'll write a generic step-by-step that you can apply to any case. Let's dive in!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Steps to create your own recursive function"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "I prepared a slightly modified version of the steps created by the one and only Dr. Graham Hutton. Renowned researcher, teacher, and board member of the Haskell Foundation. So... you know... these are the real deal:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "1. Write down the type: This will help you define de function later. (You should always define the type first, even if you're not defining a recursive function.)\n",
    "2. Enumerate the possible cases you could have based on its inputs. (Sart with the \"standard\" ones and change or refine them if needed.)\n",
    "3. Between all the previously instantiated cases, identify which are the simplest ones and define them. (These often are the base (or edge) cases.)\n",
    "4. Think about what you have available (parameters, functions, operators, other values, operators for that type, etc.).\n",
    "5. Define the rest of the cases.\n",
    "6. Reflect on the function. Can the definition be simplified? Can the signature be generalized? (we'll see how to do it in future lessons) Does it do what you intended?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "You don't always have to go through these steps. Once you feel more comfortable, you can skip a few or even write the function right off the bat."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "In general, the base (or edge) case is usually the \"identity\" case. A case that doesn't modify the result but just stops the recursion. Here we have a few examples:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Two common standard patterns:\n",
    "\n",
    "- For recursive functions that take non-negative numbers as input, you usually (not always) have a base (or edge) case of `0` or `1` (depending on the operation) and a recursive case of `n`.\n",
    "- For recursive functions that take lists as input, you usually (not always) have a base (or edge) case of `[]` (empty list) and a recursive case of `(x:xs)` (non-empty list)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, if we want to modify the `sum` function to calculate the product of the elements of the list and we just change the recursive case like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "product :: [Int] -> Int\n",
    "product [] = 0\n",
    "product (x:xs) = x * product xs -- Only changed + to *\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We'd run into the problem that the function would always return `0`. Because all the elements of the list get multiplied by `0` at the end of the recursion due to the base case!\n",
    "\n",
    "So, instead, the correct way to define the base case for `product` is to provide the \"identity\" for the product (`*`) function, which is `1`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "product :: [Int] -> Int\n",
    "product [] = 1\n",
    "product (x:xs) = x * product xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And there you go. We have our second recursive function defined.\n",
    "\n",
    "Practice is what it'll give you the intuition needed to quickly define recursive functions. So let's define a bunch of functions to get that intuition going! 💪"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Recursion examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Note: I added `'` to all the names because all these functions already exist in Haskell."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### `and'`: A function that returns returns `True` if and only if **all** the elemens of the list are `True`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, it takes a list of booleans and returns a boolean. Translating that to the type:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "and' :: [Bool] -> Bool\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, because it takes a list, we'll define the standard cases for lists:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "and' :: [Bool] -> Bool\n",
    "and' []     =\n",
    "and' (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The base case might not be that obvious. Sure, there are just two values to pick from because it's a `Bool`. But which one? So, we'll start with the recursive case.\n",
    "\n",
    "Now, let's think about what we have available to us. Because we're dealing with `Bool`, we have access to all the boolean operations. And there's one that does what we need but between just two values. The `&&` (and) operator.\n",
    "\n",
    "So, the first element combined using `&&` with the result of processing the rest of the list gives us the desired result:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "and' :: [Bool] -> Bool\n",
    "and' []     =\n",
    "and' (x:xs) = x && ...\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And, now we have to return `True` if and only if **all** the elements of the `xs` list are `True`. Meaning that we need the same function that we're defining right now. So we apply it to `xs`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "and' :: [Bool] -> Bool\n",
    "and' []     =\n",
    "and' (x:xs) = x && and' xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And now, the base case is obvious! If we use `False`, it doesn't matter which list we process, we'll always get `False` because `&& False` always equals `False`.\n",
    "\n",
    "But if we use `True`, we won't modify the result! Because the result of `&& True` depends on the missing left side. If there is a single element that isn't `True` in the list, it'll give us `False` all the way until the end. Else, it'll give us `True`! \n",
    "\n",
    "Another way of figuring this out is by figuring out that `True` is the identity for `&&`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "and' :: [Bool] -> Bool\n",
    "and' []     = True\n",
    "and' (x:xs) = x && and xs\n",
    "\n",
    "and' [True, False, True]\n",
    "and' [2 < 3, 4 == 4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### `length'`: A function that gives you the length of a list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "To calculate the length of a list, we have to take a list and return an integer. And because, in principle, we won't operate on the elements of the list, we can use a polymorphic type like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "length' :: [a] -> Int\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, because it takes a list, we'll define the standard cases for lists:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "length' :: [a] -> Int\n",
    "length' []     =\n",
    "length' (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, looking for easy cases, we can identify that the length of an empty list is, of course, `0` elements. So we replace that:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "length' :: [a] -> Int\n",
    "length' []     = 0\n",
    "length' (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And now, we can calculate the length of a list if we add `1` for each element of the list, right? And because we have the first element (`x`) singled out by pattern matching, we can add `1` for it and recursively calculate the length of the rest of the list (`xs`):"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "length' :: [a] -> Int\n",
    "length' []     = 0\n",
    "length' (x:xs) = 1 + length' xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "That one could be the final function. But because we don't actually use `x`, we can ignore it in our pattern:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "26"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "length' :: [a] -> Int\n",
    "length' []     = 0\n",
    "length' (_:xs) = 1 + length' xs\n",
    "\n",
    "length' [1,2,3,4,5]\n",
    "length' ['a'..'z']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And that's our final definition."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "##### `reverse'`: A function that reverses a list."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "To reverse a list, we take a list of elements and return a list of elements. And because, in principle, we won't operate on the elements of the list, we can use a polymorphic type like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "reverse' :: [a] -> [a]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, because it takes a list, we'll define the standard cases for lists:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "reverse' :: [a] -> [a]\n",
    "reverse' []     =\n",
    "reverse' (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The reverse of the empty list it's just the empty list. So that's the easy one. And it's also a base case because it's not recursive: "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "reverse' :: [a] -> [a]\n",
    "reverse' []     = []\n",
    "reverse' (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And now, if we take the first element, put it at the end, and keep doing that until we reach the end of the initial list, it will be reversed! So, we just need to take `x`, put it at the end, and do the same recursively until we run out of elements, which is our base case:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5,4,3,2,1]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"desserts\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "reverse' :: [a] -> [a]\n",
    "reverse' []     = []\n",
    "reverse' (x:xs) = reverse' xs ++ [x]\n",
    "\n",
    "reverse' [1,2,3,4,5]\n",
    "reverse' \"stressed\" -- What's the reverse of stressed?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Ok. We saw enough easy examples. Now let's do something a little bit more complicated:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### `drop'`: Remove the first `n` elements from a list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So it takes an integer and a list and returns a list. And because, in principle, we won't operate on the elements of the list, we can use a polymorphic type like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "drop' :: Int -> [a] -> [a]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "OK! This is new! We have two different arguments to take into account now.\n",
    "\n",
    "The way to do this is to present all possible standard pattern combinations. Because we have numbers, we initially take into account the pattern for `0` and any other number. And because we have lists, we have to take into account the pattern for empty and non-empty lists. \n",
    "\n",
    "So, we have:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "drop' :: Int -> [a] -> [a]\n",
    "drop' 0 []     =\n",
    "drop' 0 (x:xs) =\n",
    "drop' n []     =\n",
    "drop' n (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see, there're more things to take into account. But it isn't necessarily more difficult. Let's think about each case individually.\n",
    "\n",
    "1. If we drop `0` elements from an empty list, it makes sense that the result would be an empty list.\n",
    "2. If we drop `0` elements from a non-empty list, we return the same exact list.\n",
    "3. If we drop `n` elements from an empty list, we can return an error or an empty list. We choose to return the empty list.\n",
    "\n",
    "Replacing that in the definitions:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "drop' :: Int -> [a] -> [a]\n",
    "drop' 0 []     = []\n",
    "drop' 0 (x:xs) = x:xs\n",
    "drop' n []     = []\n",
    "drop' n (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "There you go. We completed 3 of the 4 cases. Now, what about when we want to drop `n` number of elements from a non-empty list?\n",
    "\n",
    "We already have the first element separated from the list. So if we remove that one is one less element to remove. But if we just do something like `drop n xs`, the function will keep dropping elements until the list is empty. \n",
    "\n",
    "Luckily, there's an easy solution. If we recursively call `drop'` with `xs`, we'd be dropping one element on each recursive call. So we can subtract `1` from `n` on each call to keep it synced. That way, if there are more than `n` elements, we'll stop the recursion when we reach `n = 0`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "drop' :: Int -> [a] -> [a]\n",
    "drop' 0 []     = []\n",
    "drop' 0 (x:xs) = x:xs\n",
    "drop' n []     = []\n",
    "drop' n (x:xs) = drop' (n - 1) xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Ok. We have a working function. But there are a few things to be improved:\n",
    "\n",
    "1. Both cases that take an empty list return an empty list. So we can ignore the `Int` in those cases.\n",
    "2. In the second case, we just pass through the input, so there's no need for pattern matching.\n",
    "3. We don't use `x` in the recursive definition, so we can also ignore it.\n",
    "\n",
    "Doing those changes, we get:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "drop' :: Int -> [a] -> [a]\n",
    "drop' _ []     = []\n",
    "drop' 0 xs     = xs\n",
    "drop' n (_:xs) = drop' (n - 1) xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "It looks like we arrived at our final `drop` definition. But did we really? What happens if `n < 0`? Theoretically, it doesn't make any sense. But in practice, someone could be crazy enough to try it!\n",
    "\n",
    "In that case, our current function will keep dropping elements one by one until it runs out because we'll never get to `n = 0`. \n",
    "\n",
    "That could be a way to handle that case. But intuitively, you'd think that dropping a negative number of elements would do the same as dropping zero elements.\n",
    "\n",
    "So we have to adjust our definition to accommodate that. And to do it, we can change the the case that handles `n == 0` to handle `n <= 0` by binding the number to the variable `n` and using guards to check for the desired property.\n",
    "\n",
    "Like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1,2,3]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"Ok, I do like chocolate.\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"Ok, I do like to write silly examples.\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "drop' :: Int -> [a] -> [a]\n",
    "drop' _ []           = []\n",
    "drop' n xs | n <= 0  = xs\n",
    "drop' n (_:xs)       = drop' (n - 1) xs\n",
    "\n",
    "\n",
    "drop' (-3) [1,2,3]\n",
    "\n",
    "yesYouDo :: String -> String\n",
    "yesYouDo = (\"Ok, I do\"++) . drop' 7\n",
    "\n",
    "yesYouDo \"I don't like chocolate.\"\n",
    "yesYouDo \"I don't like to write silly examples.\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And now the function does work as intended!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### `take'`: Take (and return) the first `n` elements from a list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This function is oddly similar to `drop'`. It takes an integer and a list and returns a list. But this time, the list contains all the elements from the first one until `n`. Because we just saw a similar case, we'll do the first and second steps together:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "take' :: Int -> [a] -> [a]\n",
    "take' 0 []     =\n",
    "take' 0 (x:xs) =\n",
    "take' n []     =\n",
    "take' n (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Same as before, let's think about each case individually:\n",
    "\n",
    "1. If we take `0` elements from an empty list, it makes sense that the result would be an empty list.\n",
    "2. If we take `0` elements from a non-empty list, we take nothing, so we return an empty list.\n",
    "3. If we take `n` elements from an empty list, we can return an error or an empty list. We choose to return the empty list.\n",
    "\n",
    "So, replacing that:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "take' :: Int -> [a] -> [a]\n",
    "take' 0 []     = []\n",
    "take' 0 (x:xs) = []\n",
    "take' n []     = []\n",
    "take' n (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Well, that was easy. Now, for the recursive case. Like the last time, we also need to reduce `n` by one on each step. But, unlike the last time, now we want to keep the elements on each step. And there's an easy way to do it. \n",
    "\n",
    "We can prepend them to a new list that will keep getting recursively bigger until we either reach `n = 0` or run out of elements in the list:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "take' :: Int -> [a] -> [a]\n",
    "take' 0 []     = []\n",
    "take' 0 (x:xs) = []\n",
    "take' n []     = []\n",
    "take' n (x:xs) = x : take' (n-1) xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, we can simplify the expression:\n",
    "\n",
    "1. If `n = 0`, we don't care about the list. We'll return an empty list anyway.\n",
    "2. If the list is empty, we don't care about the number. We'll return an empty list anyway.\n",
    "\n",
    "Translated to code:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "take' :: Int -> [a] -> [a]\n",
    "take' 0 _      = []\n",
    "take' _ []     = []\n",
    "take' n (x:xs) = x : take' (n-1) xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We do have the same problem as we did with `drop`. Intuitively, taking a negative number of elements should do the same as taking zero elements. It should not return the whole list.\n",
    "\n",
    "Luckily, we already know how to solve this problem. Same as with `drop`'s definition:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1,2,3]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "take' :: Int -> [a] -> [a]\n",
    "take' n _      | n <= 0 = []\n",
    "take' _ []              = []\n",
    "take' n (x:xs)          = x : take' (n-1) xs\n",
    "\n",
    "take' 3 [1,2,3,4,5]\n",
    "take' (-3) [1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### `map'`:  A higher-order function that applies a function to every element on a list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As always, let's start with the type. We'll have a function and a list and will return a list. Because we don't know the function that will be passed as an argument, we'll use polymorphic type variables. So the type is:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "map' :: (a -> b) -> [a] -> [b]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, let's enumerate the cases. In the case of a function, there's only one case. You get the function. So, taking into account \"estandard\" the cases for lists, we get:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "map' :: (a -> b) -> [a] -> [b]\n",
    "map' f []     =\n",
    "map' f (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If we don't have elements on the list, we just return the empty list. Which will be our base case. And also, we won't be using the function in this case, so we can ignore it:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "map' :: (a -> b) -> [a] -> [b]\n",
    "map' _ []     = []\n",
    "map' f (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now for the recursive case, we have to apply the function `f` to every element and return the list. So we could apply `f` to the first element (`x`) and prepend it to the recursive use of `map'` applied to the rest of the list (`xs`):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2,3,4,5]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[\"Hey!\",\"Ho!\",\"Let's go!\"]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "map' :: (a -> b) -> [a] -> [b]\n",
    "map' _ []     = []\n",
    "map' f (x:xs) = f x : map' f xs\n",
    "\n",
    "\n",
    "map' (+1) [1,2,3,4]\n",
    "map' (++\"!\") [\"Hey\",\"Ho\",\"Let's go\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This is an incredibly useful function. You'll use it quite often!\n",
    "\n",
    "Now, let's do one last recursive definition before learning about folds!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### `filter'`: Filter the elements of a list that don't satisfy a predicate."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We used this function quite a lot. So you know how it works. It takes a predicate and a list and returns a list with only the elements that satisfy that predicate:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "filter' :: (a -> Bool) -> [a] -> [a]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, if we enumerate the cases, the first parameter is a function, so there's only one case, and the second is a list, so it can be an empty list or a non-empty list:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "filter' :: (a -> Bool) -> [a] -> [a]\n",
    "filter' p []     =\n",
    "filter' p (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Because we don't have elements to be filtered in the first case, we return an empty list. And because we won't be using the predicate, we can ignore it. It's starting to feel easy, right?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "filter' :: (a -> Bool) -> [a] -> [a]\n",
    "filter' _ []     = []\n",
    "filter' p (x:xs) =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now let's work through the recursive case.\n",
    "\n",
    "In this case, we have two situations. One is that the element does satisfy the predicate, and the other is that it doesn't. We could convey this in different ways. I prefer using guards:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "filter' :: (a -> Bool) -> [a] -> [a]\n",
    "filter' _ []     = []\n",
    "filter' p (x:xs)\n",
    "    | p x       =\n",
    "    | otherwise =\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, if the predicate `p` applied to the first element `x` returns `True`, we add the element to the list that we'll return at the end. Otherwise, we don't. And in both cases, we recursively apply `filter'` to the rest of the elements (`xs`).\n",
    "\n",
    "\n",
    "Translating this to code, we get:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[True,True,True]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[\"Hey!\"]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[1.0,2.0,3.0,4.0,5.0,6.0]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "filter' :: (a -> Bool) -> [a] -> [a]\n",
    "filter' _ []     = []\n",
    "filter' p (x:xs)\n",
    "    | p x       = x : filter' p xs\n",
    "    | otherwise = filter' p xs\n",
    "    \n",
    "\n",
    "filter' (==True) [True,False,True,True,False]\n",
    "filter' ('!' `elem`) [\"Hey!\", \"How are you?\"]\n",
    "filter' (\\x -> x**2 < 37) [1,2,3,4,5,6,7,8,9,10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And that's it! You can filter away!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Ok. We created enough recursive functions to start noticing some patterns. So, let's talk about that."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Extracting the `foldr` pattern"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Take a look at these previously defined functions. See if you can spot a pattern:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "sum' :: [Int] -> Int\n",
    "sum' []     = 0\n",
    "sum' (x:xs) = x + sum' xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "product' :: [Int] -> Int\n",
    "product' []     = 1\n",
    "product' (x:xs) = x * product' xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "and' :: [Bool] -> Bool\n",
    "and' []     =  True\n",
    "and' (x:xs) =  x && and' xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see, there is a pattern that repeats in every function!:\n",
    "\n",
    "1. There's a base case for an empty list that returns a non-recursive value.\n",
    "2. There's a recursive case for a non-empty list that takes the first value of the list and applies a function to combine it with a recursive call that processes the rest of the list.\n",
    "\n",
    "This pattern has a name! It's called \"primitive recursion.\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "By now, you know the drill. We're going to extract the pattern into its own function! But first, notice that this pattern assumes that the function that combines the values on the recursive case is an operator. To make it more general, let's modify them to use prefix funcitons before extracting it:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "sum' :: [Int] -> Int\n",
    "sum' [] = 0\n",
    "sum' (x:xs) = (+) x (sum' xs)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "product' :: [Int] -> Int\n",
    "product' [] = 1\n",
    "product' (x:xs) = (*) x (product' xs)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "and' :: [Bool] -> Bool\n",
    "and' []     =  True\n",
    "and' (x:xs) =  (&&) x (and' xs)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We're going to call the abstraction `foldr` (duh) cause we're folding the list from the right. You'll see what I mean.\n",
    "\n",
    "As always, (first, we start with the type. So, we need 3 arguments:\n",
    "1. A function to combine the elements of the list. So, it should take two elements and generate a new one.\n",
    "2. A base value to start from.\n",
    "3. A list.\n",
    "\n",
    "Notice that the elements inside the lists can be anything, but not necessarily of the same type as the result. (We don't know what the function will do.) So, we'll use type `a` for elemes of the list and type `b` for the result. And from that follows that the base value has to be of type `b` and the function has to be of type `a -> b -> b`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "foldr :: (a -> b -> b) -> b -> [a] -> b\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Ok, now, let's extract the pattern into it's own function. Let's start by presenting the pattern, and we'll go from there:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "foldr :: (a -> b -> b) -> b -> [a] -> b\n",
    "foldr f v [] =  -- base value\n",
    "foldr f v (x:xs) = --function combining value and recursion\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We already have the base value (`v`). It's one of the arguments. And the recursive call is just applying the function `f` to `x` and a recursive call of `foldr` but with `xs` instead of the original list. So we can do just that in the definition:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "foldr :: (a -> b -> b) -> b -> [a] -> b\n",
    "foldr _ v [] =  v\n",
    "foldr f v (x:xs) = f x (foldr f v xs)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Done! We just extracted the \"primitive recursion\" pattern!\n",
    "\n",
    "To demonstrate that it's actually the same, we'll pass the parameters needed to create the `sum` function and work through an example:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "-- same as: sum [1,2,3,4]\n",
    "foldr (+) 0 [1,2,3,4] = (+) 1 (foldr (+) 0 [2,3,4])\n",
    "                      = (+) 1 ((+) 2 (foldr (+) 0 [3,4]))\n",
    "                      = (+) 1 ((+) 2 ((+) 3 (foldr (+) 0 [4])))\n",
    "                      = (+) 1 ((+) 2 ((+) 3 ((+) 4 (foldr (+) 0 []))))\n",
    "                      = (+) 1 ((+) 2 ((+) 3 ((+) 4 0))) -- 1 + ( 2 + ( 3 + ( 4 + 0 )))\n",
    "                      = (+) 1 ((+) 2 ((+) 3 4)) -- 1 + ( 2 + ( 3 + 4 ))\n",
    "                      = (+) 1 ((+) 2 7) -- 1 + ( 2 + 7 )\n",
    "                      = (+) 1 9 -- 1 + 9\n",
    "                      = 10\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Worked like a charm!\n",
    "\n",
    "Now, we can replace it in our previous definitions to get a much clear and more concise code:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "sum' :: [Int] -> Int\n",
    "sum' = foldr (+) 0 -- We partially apply foldr\n",
    "\n",
    "\n",
    "product' :: [Int] -> Int\n",
    "product' = foldr (*) 1\n",
    "\n",
    "\n",
    "and' :: [Bool] -> Bool\n",
    "and' = foldr (&&) True\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If, while defining a recursive function, you find out that you're using this pattern, use `foldr` instead! That way, everyone (including you two months later) will instantly understand what the function does without needing to figure out the recursion."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Speaking of which, the `length'` function fits almost perfectly!:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "length' :: [a] -> Int\n",
    "length' []     = 0\n",
    "length' (_:xs) = (+) 1 (length' xs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The only difference is that we ignore `x` and add a constant value instead. If we could just hardcode the first parameter of the `+` operator... that would be perfect! Well, why don't we create a function that does just that and passes that one instead of `+`? We just need to take two parameters, ignore the first one, and add `1` to the second parameter! We can easily do that with a quick lambda function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "length' :: [a] -> Int\n",
    "length' []     = 0\n",
    "length' (x:xs) = (\\_ n -> 1 + n) x (length' xs) --lambda could be simplified to (\\_ -> (+) 1)\n",
    "\n",
    "length' [1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And Boom! Just like that, `length'` perfectly fits the pattern! So we can replace it with `foldr`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "length' = foldr (\\_ n -> 1 + n) 0\n",
    "\n",
    "length' [1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see, there's certain flexibility. Let's re-implement reverse but with `foldr`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5,4,3,2,1]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "reverse' :: [a] -> [a]\n",
    "reverse' = foldr (\\x xs -> xs ++ [x]) []\n",
    "\n",
    "reverse' [1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "It seems that we could use `foldr` all day long. But it's not all roses. If, for example, use `reverse'` with a thousand, ten thousand, or even more numbers, the toll of using `++` grows bigger and bigger. \n",
    "\n",
    "Why? Well... let's see how `++` is defined in the base library:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "(++) :: [a] -> [a] -> [a]\n",
    "(++) []     ys = ys\n",
    "(++) (x:xs) ys = x : xs ++ ys\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see in the recursive case, each time we want to add two lists, first, we walk through all the elements of the first list, and then we add the second list at the end. So, if we have a list 10X bigger, we have to wait 10 times more for it to complete. Meaning that it takes linear time in the number of elements of the first list."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "What does that mean to us? It means that, on `reverse'`'s recursive call, each time we want to move an element from the front to the back of the list (every time we do a recursive call), we have to walk through the entire list! Every time! If the list is long enough, you could go for a run while waiting for it to be reversed!\n",
    "\n",
    "But don't worry. I wouldn't leave you hanging like that. There's a neat solution to this. If we could walk through the list from left to right instead of from right to left, we could use the cons (`:`) operator instead of `++`, and in each recursive call, we would add the element at the very beginning. No walking through the entire list is needed!\n",
    "\n",
    "Enter the `foldl` function!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## The `foldl` function"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "`foldl` does essentially the same as `foldr` but traverses the list from left to right:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "foldr :: (a -> b -> b) -> b -> [a] -> b\n",
    "foldr f v [] =  v\n",
    "foldr f v (x:xs) = f x (foldr f v xs)\n",
    "\n",
    "\n",
    "foldl :: (a -> b -> a) -> a -> [b] -> a\n",
    "foldl f v [] = v\n",
    "foldl f v (x:xs) = foldl f (f v x) xs\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "For example, let's see what happens step by step when we replace `foldr` with `foldl` in the `sum` function:\n",
    "\n",
    "(Notice how the second argument keeps growing while the third argument keeps getting smaller.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "foldl (+) 0 [1,2,3,4] = foldl (+) ((+) 0 1) [2,3,4]\n",
    "                      = foldl (+) ((+) ((+) 0 1) 2) [3,4]\n",
    "                      = foldl (+) ((+) ((+) ((+) 0 1) 2) 3) [4]\n",
    "                      = foldl (+) ((+) ((+) ((+) ((+) 0 1) 2) 3) 4) []\n",
    "                      = (+) ((+) ((+) ((+) 0 1) 2) 3) 4 -- ((( 0 + 1 ) + 2 ) + 3 ) + 4\n",
    "                      = (+) ((+) ((+) 1 2) 3) 4 -- ((1 + 2 ) + 3 ) + 4\n",
    "                      = (+) ((+) 3 3) 4 -- (3 + 3 ) + 4\n",
    "                      = (+) 6 4 -- 6 + 4\n",
    "                      = 10\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And that's how `foldl` works.\n",
    "\n",
    "And because now we can traverse the list from left to right, we can use the `:` (cons) operator to join values instead of `++`.\n",
    "\n",
    "Taking that into account, we can write `reverse'` like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5,4,3,2,1]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "reverse'' :: [a] -> [a] \n",
    "reverse'' = foldl (\\x y -> y:x) []  -- Same as: foldl (flip (:)) []\n",
    "\n",
    "reverse'' [1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And now, we can compare the speed of the two functions by reversing a list from 1 to 10.000! Run the two cells separately and see the speed difference:\n",
    "\n",
    "(We use `sum` to avoid printing the entire list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50005000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sum . reverse' $ [1..10000] -- With foldr and (++)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50005000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sum . reverse'' $ [1..10000] -- With foldl and (:)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "An impressive improvement! But not the only thing that differs between `foldr` and `foldl`!\n",
    "\n",
    "So far, we haven't encountered this because, for example, the addition operator (`+`) returns the same either way:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "foldr (+) 0 [4,3,2,1] == foldl (+) 0 [4,3,2,1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "But, for some operators, the order of the operation can give different results depending on the direction! For example, consider `(-)` instead of `(+)`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "foldr (-) 0 [4,3,2,1] == foldl (-) 0 [4,3,2,1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This is false because if we write the operations out explicitly, we get:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "foldl (-) 0 [4,3,2,1] = (((0-4)-3)-2)-1 = -10\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "while"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "foldr (-) 0 [4,3,2,1] = 4-(3-(2-(1-0))) = 2\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So that's another thing to take into account.\n",
    "\n",
    "And lastly, there's one last thing I want to talk about. And that's `foldl'`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## The `foldl'` function"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "All the functions we defined so far had the `'` at the end because they already existed in Haskell, and we didn't want to get a collision. But! `foldl'` is also a function that comes with Haskell, and it works a little differently than `foldl`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "In both `foldr` and `foldl` cases, we saw that we kept stacking up expressions until the end. And then we reduce them. (Actually, Haskell does all the job, not us. But you get the point.)\n",
    "\n",
    "This means that if you try to fold a big enough list, you'll get a `stack overflow` exception!\n",
    "\n",
    "If we pick any intermediate step in `foldr'`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "-- Same as:             (+) 1 ((+) 2 ((+) 3 (foldr (+) 0 [4])))\n",
    "foldr (+) 0 [1,2,3,4] = 1 + (2 + (3 + (foldr (+) 0 [4]))) \n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We see that we can't do much for `foldr` since we don't have a single operator with both arguments. So we'll always need to resolve the recursive function first.\n",
    "\n",
    "But! If we take a look at the same intermediate step in `foldl`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "-- Same as:             foldl (+) ((+) ((+) ((+) 0 1) 2) 3) [4]\n",
    "foldl (+) 0 [1,2,3,4] = foldl (+) (((0 + 1) + 2) + 3) [4]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We could totally reduce `(((0 + 1) + 2) + 3)` to `6` before continuing with the recursion!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And that's what `foldl'` does!\n",
    "\n",
    "To be clear: `foldl` and `foldl'` return the same result! The diference is that `foldl'` reduces expressions at intermediate steps. So it's more efficient because it doesn't build a huge thunk!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, if we run something like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "foldl (+) 0 [1..1000000] -- Don't run it! I'm warning you!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "You'll get a stack overflow exception. But if you use `foldl'` instead:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "500000500000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import Data.List\n",
    "\n",
    "foldl' (+) 0 [1..1000000]  -- No problems!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "You'll face no issues."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And this raises a question. When should you use each one?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## When to use `foldr`, `foldl`, and `foldl'`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Usually, the choice is between `foldr` and `foldl'`, since `foldl` and `foldl'` are the same except for their strictness properties. So, if both return a result, `foldl'` is the more efficient way to arrive at that result because it doesn't build a huge thunk.\n",
    "\n",
    "However, that's not the whole story. We're going to give some rules of thumb from least to most used fold:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Use `foldl`:\n",
    "- Rarely. \n",
    "- If the combining function is lazy in its first argument. (`foldl` may return a result where `foldl'` hits an exception.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Use `foldl'`:\n",
    "- When the list to which it is applied is large but definitely finite, you do not care about the implicit reversal (for example, because your combining function is commutative), and you seek to improve the performance of your code.\n",
    "- When you actually do want to reverse the order of the list in addition to possibly performing some other transformation to the elements. (Taking advantage of the implicit reverse.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Use `foldr`:\n",
    "\n",
    "- When transforming lists into lists with related elements in the same order.\n",
    "- When transforming infinite lists into other infinite lists. (If the function passed is lazy in its second argument, `foldr` will lazily generate the result, computing only as much as is required.) \n",
    "- When the folding function can short-circuit (terminate early) by yielding a result that does not depend on the value of the accumulating parameter.\n",
    "- If you're not sure."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "These rules of thumb do not necessarily always apply. And because going through all the whys of these rules could take a whole class, we'll leave it for the curious or for when you happen to need it. [Here's more information on the subject](https://wiki.haskell.org/Foldr_Foldl_Foldl')."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# That's it for today!"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Haskell",
   "language": "haskell",
   "name": "haskell"
  },
  "language_info": {
   "codemirror_mode": "ihaskell",
   "file_extension": ".hs",
   "mimetype": "text/x-haskell",
   "name": "haskell",
   "pygments_lexer": "Haskell",
   "version": "8.10.7"
  },
  "rise": {
   "enable_chalkboard": true,
   "header": "<img style=\"position: relative; left: 1230px; width: 200px; top: 10px;\" src=\"https://raw.githubusercontent.com/rober-m/haskell-bootcamp/main/images/input-output.svg\"/>"
  },
  "vscode": {
   "interpreter": {
    "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
