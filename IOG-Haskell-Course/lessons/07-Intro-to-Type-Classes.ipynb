{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Intro to Type Classes"
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
    "* The awesomeness of type classes\n",
    "* What are type classes \n",
    "* Common type classes \n",
    "\t* `Eq`, `Ord`\n",
    "    * `Num`, `Integral`, `Floating`\n",
    "\t* `Read`, `Show`\n",
    "* The most general valid type\n",
    "* Multiple constraints"
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
    "<div class=\"alert alert-block alert-info\">\n",
    "<p>\n",
    "This is an introduction to the concept and use of type classes from the consumer's point of view. Meaning that, as we are developing in Haskell, there are type classes, and we want to understand and use them.\n",
    "</p>\n",
    "<p>\n",
    "Two lessons from now, after learning about how to create types, we'll look at it from the point of view of the type class and instance creator.\n",
    "</p>\n",
    "</div>"
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
    "## The awesomeness of type classes"
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
    "So far, we learned that, when defining a function, we choose that it could be used either with a specific type like this:"
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
    "sqr :: Int -> Int\n",
    "sqr v = v * v\n",
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
    "Which provides a lot of safety because by making sure that your function only takes `Int` types, no matter the value it takes, you can do math with it. But the downside is that you're constrained to use that function with only that type. If you need it for `Double` or `Float,` you have to define it again with a different name like `sqrDouble` and `sqrFloat`.\n",
    "\n",
    "Or with a polymorphic type like this:"
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
    "```Haskell\n",
    "fst :: (a, b) -> a\n",
    "fst (x, _) = x\n",
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
    "Which provides a lot of flexibility because you can use values of any type as input, but you lose all the safety that comes with using types. \n",
    "\n",
    "So, we have something like this:"
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
    "```\n",
    "                    ↑\n",
    "                    | X (Polym.)    \n",
    "                    |\n",
    "      Flexibility   |\n",
    "                    |\n",
    "                    |\n",
    "                    |                X (Types)     \n",
    "                    |\n",
    "                    ------------------⟶\n",
    "                             Safety\n",
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
    "Type classes are what you get when you're a stubborn programming language developer and want the flexibility of having polymorphic types and the safety of using types all at the same time."
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
    "```\n",
    "                    ↑\n",
    "                    | X (Polym.)     X (Type Classes)\n",
    "                    |\n",
    "      Flexibility   |\n",
    "                    |\n",
    "                    |\n",
    "                    |                X (Types)     \n",
    "                    |\n",
    "                    ------------------⟶\n",
    "                             Safety\n",
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
    "At the end of the day, what Type Classes do is allow you to use **restricted polymorophic values**. Values can be of different types, but not all of them. Just an authorized subset. This is called *Ad-hoc polymorphism* or *overloading*, but you don't need to remember that right now."
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
    "Now that we know why type classes are awesome, let's see what they actually are!"
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
    "## What are type classes?"
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
    "If you meet people that belong to the advanced-drawing club, you know they can draw. Why? Because it's one of the requirements to enter the club!"
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
    "Type classes are like clubs that types can belong to if they have particular behaviors. (Behavior, in this context, means function.) So, a type class specifies a bunch of functions, and each type that belongs to the type class has its own definitions of those functions."
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
    "So, from the point of view of the developer that consumes pre-existing types and type classes:"
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
    "**If you see that a type is an Instance of a type class, you know that it implements and supports the behaviors (functions) of that type class.**"
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
    "For example, the `Bool` type. To see the type classes to which the `Bool` type belongs, you can use the `:i` (info) command in ghci. If we run `:i Bool`, we get:"
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
    "type Bool :: *\n",
    "data Bool = False | True\n",
    "  \t-- Defined in ‘GHC.Types’\n",
    "instance Eq Bool -- Defined in ‘GHC.Classes’\n",
    "instance Ord Bool -- Defined in ‘GHC.Classes’\n",
    "instance Enum Bool -- Defined in ‘GHC.Enum’\n",
    "instance Show Bool -- Defined in ‘GHC.Show’\n",
    "instance Read Bool -- Defined in ‘GHC.Read’\n",
    "instance Bounded Bool -- Defined in ‘GHC.Enum’\n",
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
    "We'll learn about `type` and `data` in the next lesson. So, if we ignore the first two lines of code, we see a bunch of lines that say `instance ...`. Those lines inform us that the `Bool` type is an instance of the `Eq` type class, the `Ord` type class, etc.\n",
    "\n",
    "So, `Bool` implements the functions of all those type classes. And, naturally, now we want to know what the behaviors those type classes define. So let's find out!"
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
    "## Common type classes"
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
    "Now, we're going to go through the most common type classes. And I'm going to tell you what they represent and their main behaviors. But you don't have to memorize anything about this. After the \"creating type classes\" lesson, you'll be able to swiftly check everything I'll say in this class. Also, don't worry about the details just yet. We'll spend this and two more lessons on the type system. Use this lesson to start developing the idea of a type class and to get familiar with the most common built-in ones (which are usually the only ones you need)."
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
    "### The `Eq` type class"
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
    "The `Eq` type class is all about equality. The types that are instances of the `Eq` type class can say if two values of its type are equal or not by using the `==` (equal) and `/=` (not equal) functions."
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
    "And because the `Bool` type is an instance of `Eq`, we know that we can use those two functions to compare values of that type:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "True == False  -- False\n",
    "\n",
    "True /= False  -- True"
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
    "And if we check the signatures of the `==` and `/=` functions, we'll see a few new things:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    },
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "source": [
    "```haskell\n",
    "(==) :: Eq a => a -> a -> Bool\n",
    "\n",
    "(/=) :: Eq a => a -> a -> Bool\n",
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
    "The `=>` symbol is the **class constraint** symbol. It indicates that **a polymorphic type is constrained to be an instance of a type class**."
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
    "The code to the right of the fat arrow (`=>`) is the same type signature we've used so far. And the code to the left of the fat arrow (`=>`) indicates the class constraints.\n",
    "\n",
    "In this case, the code to the right of the fat arrow (`a -> a -> Bool`) indicates that these functions take two polymorphic values and return a `Bool`. Same as always. And the code to the left of the fat arrow (`Eq a`) indicates that the type `a` that is used twice at the right of the fat arrow has to be an instance of the type class `Eq`. \n",
    "\n",
    "So, we're constraining (limiting) the types you can pass to these two functions, from all the types to only those that are instances of the `Eq` type class."
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
    "And it doesn't stop there. For example, imagine you create this function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "func x y = if x == y then x else y"
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
    "You don't do math or manipulate strings. **But you do check if the values are equal. So you want to make sure that this function only accepts values that can be checked for equality**. That's what the `Eq` type class constraint is for. To block you from using types with values that can't be compared.\n",
    "\n",
    "And because `==` has the `Eq a` constraint and `func` uses `==` inside, Haskell is smart enough to infer that our function's type signature also has that constraint:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "func :: Eq a => a -> a -> a\n",
    "func x y = if x == y then x else y"
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
    "And now comes the moment of truth. To how many types can I apply these functions? We know that we can apply it to `Bool` because `Bool` is an instance of `Eq`. But what else? Which are the other instances?"
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
    "Well.. if you use the `:i Eq` command, you'll see a huge list of all the types that are instances of this type class:"
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
    "-- ...\n",
    "instance Eq a => Eq [a] -- Defined in ‘GHC.Classes’\n",
    "instance Eq Word -- Defined in ‘GHC.Classes’\n",
    "instance Eq Ordering -- Defined in ‘GHC.Classes’\n",
    "instance Eq Int -- Defined in ‘GHC.Classes’\n",
    "instance Eq Float -- Defined in ‘GHC.Classes’\n",
    "instance Eq Double -- Defined in ‘GHC.Classes’\n",
    "instance Eq Char -- Defined in ‘GHC.Classes’\n",
    "instance Eq Bool -- Defined in ‘GHC.Classes’\n",
    "-- ... more instances\n",
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
    "As you can see, all the types we encountered so far (and more) are instances of this type class (except for functions). That's why we can check if two values of type `Char`, `Int`, `Float`, etc are equal or not, and that's why we can apply the function `func` we just defined to any of them:"
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
    "func True False -- False\n",
    "\n",
    "func 1 2        -- 2\n",
    "\n",
    "func 1.0 1.0    -- 1.0\n",
    "\n",
    "func 'a' 'c'    -- 'c'"
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
    "And if you happen to pass a value that isn't an instance of `Eq`, like a function:"
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
    "f1 x = x + 1\n",
    "f2 x = x + 2 - 1\n",
    "\n",
    "func f1 f2"
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
    "You'll get the error:"
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
    "No instance for (Eq (Integer -> Integer))\n",
    "        arising from a use of ‘==’\n",
    "        (maybe you haven't applied a function to enough arguments?)\n",
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
    "Because, like the error says, the type `Integer -> Integer` is not an instance of `Eq`, and we needed to be because we're using `==`."
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
    "That's really cool, but you can't do much with types that belong only to the `Eq` type class. You can only tell if two values are equal or not. That's it. Luckily, `Eq` is not the only club in town!"
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
    "### The `Ord` type class"
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
    "The `Ord` type class is all about ordering. The types that are instances of the `Ord` type class can order their values and say which value is the biggest."
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
    "And for that, the `Ord` class has all these functions:"
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
    "  (<), (<=), (>=), (>) :: Ord a => a -> a -> Bool\n",
    "  max, min             :: Ord a => a -> a -> a\n",
    "  compare              :: Ord a => a -> a -> Ordering\n",
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
    "We've already used the inequality operators ( `<`, `>`, `<=`, `>=`) in previous lessons. They take two values of the same type that belong to the `Ord` type class and return a boolean:"
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
    "4 > 9      -- False\n",
    "\n",
    "'a' >= 'b' -- False"
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
    "And how are the values ordered? It depends on the type. With numbers, it follows the mathematical order (e.g., `4` comes before `5` and after `3`). With characters, it follows the Unicode order. And other types have other rankings. As we said, each type that belongs to a type class has its own implementations (definitions) of those functions. We'll learn more about it when creating our own instances."
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
    "But with the ability to order things around, we can do more than just inequality."
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
    "#### The `min` and `max` functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    },
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "source": [
    "The `min` function takes two values of a type that is an instance of `Ord` and returns the minimum of the two:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    },
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "source": [
    "```haskell\n",
    "min :: Ord a => a -> a -> a\n",
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
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "min 12 19 -- 12"
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
    "The `max` function takes two values of a type that is an instance of `Ord` and returns the maximum of the two:"
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
    "max :: Ord a => a -> a -> a\n",
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
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "max 12 19 -- 19"
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
    "#### The `compare` function"
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
    "The `compare` function takes two values of a type that is an instance of `Ord` and returns a value of type `Ordering`, indicating the order of the values."
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
    "compare :: Ord a => a -> a -> Ordering\n",
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
    "In the same way that `Bool` has only two values (`True` and `False`), the `Ordering` type has only three values: `LT` (lesser than), `EQ` (equal), and `GT` (greater than)."
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
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "compare 4 9         -- LT (4 is lesser than 9)\n",
    "\n",
    "'f' `compare` 'e'   -- GT ('f' is greater than 'e')\n",
    "\n",
    "True `compare` True -- EQ ( True is equal to True)"
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
    "Again, so far, all the types we learned are instances of this class type (except for functions)."
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
    "Now, you might say: \"If I can check `EQ` with the `Ord` type class, why do I need the `Eq` type class?\""
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
    "Sometimes a type has to first be an instance of one type class to be allowed to become an instance of another. Like you have to belong to the doodling club to be allowed to apply to the drawing club.\n",
    "\n",
    "That's the case with `Eq` and `Ord`.\n",
    "\n",
    "To order values of a type, for starters, you have to be able to tell if they are equal or not. This tells us that if we have a type that is an instance of `Ord`, it also supports all the `Eq` behavior! In these cases, we say that `Eq` is a superclass of `Ord` (conversely, `Ord` is a subclass of `Eq`).\n",
    "\n",
    "Again, you don't need to memorize all these. Initially, you'll be able to quickly check it, and with a little bit of time, you'll know all the behaviors and subclasses by heart.\n",
    "\n",
    "Something similar occurs with numeric type classes."
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
    "### The `Num` type class"
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
    "Numeric types are one of the most used types in any programming language. But not all numeric types can do the same things."
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
    "Types that are instances of the `Num` type class can behave like numbers. But not like a specific subset of numbers. The `Num` type class defines the behavior that all numbers should have."
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
    "For example, types that are instances of this type class can be (among other things) added, subtracted, or multiplied:"
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
    "(+) :: Num a => a -> a -> a\n",
    "\n",
    "(-) :: Num a => a -> a -> a\n",
    "\n",
    "(*) :: Num a => a -> a -> a\n",
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
    "For example:"
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
    "5 - 1      -- 4\n",
    "\n",
    "8.9 + 0.1  -- 9.0\n",
    "\n",
    "'a' - 'b'  -- ERROR! Char is not an instance of Num!\n"
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
    "Now we're talking! Imagine I want to create a function that does some math:"
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
    "add1 x = x + 1"
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
    "I don't want to choose a type like `Int` and only allow `Int` values. `Float`, `Double`, and `Integer` types could work perfectly fine! But, if there were no constraints, I could pass any type! What's the result of `'a' + 'b'`? Or `True + False`? It doesn't make any sense!"
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
    "Because only types that are instances of the `Num` type class can use `+`, and because `Float`, `Double`, `Int`, and `Integer` are all instances of `Num`, we can constraint our function like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "add1 :: Num a => a -> a\n",
    "add1 x = x + 1"
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
    "But remember that if you're not sure of the type signature, ask the compiler! It knows that to use `+`, you have to be an instance of the `Num` type, so it infers the type signature of `add1` automatically! Providing flexibility and protecting us at the same time."
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
    "This is cool. But, sometimes, we need something more specific."
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
    "### The `Integral` type class"
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
    "The `Num` type class includes all the numbers, but the `Integral` type class only the integral (whole) numbers. Such as `4`, but not `4.3`."
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
    "`Integral` is a more exclusive club than `Num`. Of all the types we saw so far, only `Int` and `Integer` belong to it."
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
    "This type class defines many behaviors, one of the most well-known `Integral` functions is `div`."
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
    "div :: Integral a => a -> a -> a\n",
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
    "It takes two values of a type that is an instance of `Integral` and divides them, returning only the whole part of the division."
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
    "Examples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "3 `div` 5    -- 0\n",
    "\n",
    "div 5 2      -- 2"
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
    "And, on the flip side, we have the `Fractional` type class."
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
    "### The `Fractional` type class"
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
    "The `Fractional` type class is all about fractional numbers. The types that are instances of the `Fractional` type class can represent and modify fractional values."
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
    "By far, the most used function that instances of the `Fractional` type class is `/`:"
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
    "(/) :: Fractional a => a -> a -> a\n",
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
    "The all-mighty division. Unlike `div`, we can be more precise about our values because we're using fractional numbers. And only `Float` and `Double` are instances of this type class."
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
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "10 / 5  -- 2.0\n",
    "\n",
    "5  / 2  -- 2.5\n",
    "\n",
    "10 / 3  -- 3.3333333333333335"
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
    "Notice that we never had to specify the type of the numeric values in any of the examples so far. That's because, for example, the number `3` can be a value of type `Int`, `Integer`, `Float`, `Double`, and by applying certain functions, like `/`, the compiler can figure out that we meant the value `3` that belongs to one of the types that are instances of `Fractional`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    ":t (10/3) -- (10/3) :: Fractional a => a"
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
    "### The `Show` type class"
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
    "The `Show` type class is used to convert values to readable `String`s. It has 3 different behaviours, but the one you're going to see over and over is the `show` function:"
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
    "show :: Show a => a -> String\n",
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
    "The `show` function returns a `String` representation of any type that is an instance of the `Show` type class. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "show (3 :: Int) -- \"3\"\n",
    "\n",
    "show True       -- \"True\""
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
    "This is really useful for debugging and printing logs."
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
    "### The `Read` type class"
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
    "The `Read` type class provides the opposite behavior of the `Show` type class. Meaning it takes a `String` and returns a value of the type we ask for, if possible. The most often used behaviour is the `read` function:"
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
    "read :: Read a => String -> a \n",
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
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "read \"3\" / 2  -- 1.5\n",
    "\n",
    "read \"True\" || False  -- True\n",
    "\n",
    "read \"[1,2,3]\" :: [Int]  -- [1,2,3]"
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
    "Keep in mind that if the `String` doesn't contain a valid value or the `read` function doesn't know the type that needs to be returned, it will throw an exception:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "read \"3\" -- Doesn't know which numeric type. Exception.\n",
    "\n",
    "read \"Turue\" :: Bool -- \"Turue\" is not a valid Bool value. Exception."
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
    "You can find a detailed description of a type class if you search it on Hoogle: https://hoogle.haskell.org/."
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
    "Now, let's take a look at how the compiler infers types."
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
    "## The most general valid type"
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
    "What's the signature of this function?\n",
    "\n",
    "```haskell\n",
    "fToC x = (x - 32)*5/9\n",
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
    "The `fToC` function could have a few different types. `fToC :: Float -> Float`, for example.\n",
    "\n",
    "But, while doing type inference, the compiler assumes nothing and constrains the function's type as little as possible. Giving you the most general constraint."
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
    "Let's do it step by step."
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
    "So, in this case, the function takes a value and returns a value. So, the most general signature would be one:"
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
    "fToC :: a -> a  -- Intermediate step\n",
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
    "But, the value it takes must be a numeric type (we're applying several mathematical functions. `-`, `*`, and `/`). \n",
    "\n",
    "But which type? `Num` (because of `-` and `*`) or `Fractional` (because of `/`)?\n",
    "\n",
    "In this case, all numeric types are part of `Num`, but only `Float` and `Double` are part of `Fractional`. So, to make sure this function always works, it has to take the most restrictive type class, meaning `Fractional`:"
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
    "fToC :: Fractional a => a -> a\n",
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
    "And that's how the compiler infers the type of the expression. Notice that the type could have been even more specific, like `Float -> Float` or `Double -> Double`. But that would be assuming you need a more constrained type without evidence."
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
    "At the end of the day, the most general valid type wins."
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
    "Ok, so, until now, we've been restricting if the type is an instance of a particular type class. And we know there can be more specialized type classes (`Fractional` is a more specialized type class than `Num`)."
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
    "But what if we need a type with a more... particular set of abilities?"
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
    "## Multiple constraints"
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
    "Sometimes you need different constraints for different type variables.\n",
    "\n",
    "Or the same type variable with multiple constraints. All this can be easily expressed in Haskell."
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
    "### Multiple constraints for the same type variable"
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
    "Take this function that skips the number 3:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "skip3 x = if x == 3 then x+1 else x"
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
    "The `x` can be of any type that is an instance of `Eq` (because of `==`) and `Num` (because of `+` and because we're comparing the input with the value `3` that belongs to the `Num` type class).\n",
    "\n",
    "To specify multiple constraints for the same type variable, we have to surround them with parenthesis and add a comma between them.\n",
    "\n",
    "Like if they were a tuple:"
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
    "skip3 :: (Eq p, Num p) => p -> p\n",
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
    "Now the `p` type variable has to be a type that's an instance of both `Eq` and `Num`. And, of course, we could add more constraints if needed."
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
    "### Constraints for multiple type variables"
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
    "Let's create a function that takes two values and returns `1` if the first value is greater than the second and `0` otherwise:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "isXBigger x y = if x > y then 1 else 0"
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
    "In this case, `x` and `y` have to be instances of `Ord`. And the return value is a number of an unspecified type, so it's the more general `Num` instance.\n",
    "\n",
    "Putting this together, the type signature will be:"
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
    "isXBigger :: (Ord a, Num p) => a -> a -> p\n",
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
    "Now, let's practice just a bit. What about this function?:"
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
    "mistery1 x y z = if x > y then z/2 else z"
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
    "We compare `x` and `y` with `>`, so they have to be instances of the `Ord` type class.\n",
    "\n",
    "And the return value is divided using `/` in one of the if-else paths. So `z` has to be an instance of `Fractional`."
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
    "mistery1 :: (Ord a, Fractional p) => a -> a -> p -> p\n",
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
    "And finally, our last example is a modification of `mistery1` where we add `1` to `x` before comparing it to `y`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "mistery2 x y z = if x+1 > y then z/2 else z"
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
    "Same as before. But now `x` and `y` also have to be an instance of `Num` to be able to use `+`:"
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
    "mistery2 :: (Ord a, Num a, Fractional p) => a -> a -> p -> p\n",
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
    "As you can see, **we can apply as many constraints as needed**.\n",
    "\n",
    "Of course, in the day-to-day, the compiler can infer them for you (most of the time). But you'll still have to be aware of what's going on to correctly interpret and understand them. Also, writing a function's type before defining it is a good practice and a great way to ease up the process of defining it later."
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
  "vscode": {
   "interpreter": {
    "hash": "e7370f93d1d0cde622a1f8e1c04877d8463912d04d973331ad4851f04de6915a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
