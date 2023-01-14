# Haskell Course

[Versión en 🇪🇸](https://github.com/input-output-hk/haskell-course/tree/main/ES-translation)

**This course is designed to teach students Haskell from zero to everything needed to work with Marlowe and Plutus.** The course itself doesn't contain content specific to Marlowe or Plutus. So, if you want to use it to learn Haskell for other purposes, you can! 😃

For a more detailed explanation, keep reading or watch the introduction video:
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/H1vbUKMKvnM)

## How much should I study if I only wish to use Marlowe/Plutus?

In the [outline](#what-well-cover) below, there are clear stopping points (for both Marlowe and Plutus) where we deem you to know enough Haskell to effectively use the technology.

## How to read/watch the lessons

To go through the interactive lessons, go to your chosen lesson's outline inside "[What we'll cover](#what-well-cover)" and click on the button that looks like the one below. If the page loads with a "500: Internal Server Error" just refresh it, and it should be fine. At the top, you will see a console that displays the progress of preparing your interactive lesson. During this time, you can scroll down and look at the lesson, that is displayed non-interactively.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F01-Introduction-to-haskell.ipynb)

And to see the video, click on the button that looks like this:

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/H1vbUKMKvnM)

## To do the homework

1. Clone this repository.
2. Create a [GitPod](https://www.gitpod.io/) account.
3. Click this button to create a remote dev environment: [![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=flat&logo=visual-studio-code&logoColor=white)](https://gitpod.io/#https://github.com/input-output-hk/haskell-course)
4. Select the `Homework/HomeworkXX` folder with the homework you want to complete.
5. Follow the instructions inside the `Homework.hs` or `Main.hs` file.
6. **Check the solutions in the `solutions` branch!**

#### Repository structure

    Haskell-Course
        |   |
        |   |---- Homework
        |          |
        |          |---- Homework01 (Homework for lesson 01)
        |          |---- Homework02 (Homework for lesson 02)
        |          ...
        |
        |-------- lessons (Lessons in Jupyter notebook format. Access through Binder.)
                   |
                   |---- 1-Introduction-to-haskell
                   |---- 2-Functions-Data-Types-and-Signatures

Everything else can be safely ignored

## To hang out and discuss with other students

- [Canvas](https://iohk.instructure.com/enroll/3BAAGG)
- [IOG's technical community (check out the #ask-haskell channel!)](https://discord.gg/inputoutput)

## FAQ

[FAQ](FAQ.md)

## Proposed changes for next iteration/version

[Changes](Changes.md)

## What we'll cover

**This is a tentative outline. Changes can (and will) be made as we advance with the course and gather feedback from students.**

**If there are no buttons on a lesson, it means that it's not published yet.**

---

### START OF THE BEGINNER SECTION 🐣⟶🐥

---

### 1. Intro and tools [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F01-Introduction-to-haskell.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/pkU8eiNZipQ)

- Intro to the course and lectures
  - What we’ll cover
  - Repository structure
- Intro to Haskell
  - How to open and use JupyterLab
  - Purely functional programming language
  - Basic syntax
  - Haskell Type system
  - Laziness
  - GHC (and GHCi)
- GitPod
  - How to open and use GitPod
  - Example of how to complete a homework assignment.

### 2. Data types, Signatures, and Polymorphism [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F02-Functions-Data-Types-and-Signatures.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/RABzYje2d2A)

- Pragmatic intro to types
- Type signature
  - Function’s signatures
  - Variables in Haskell
    - Parameters in functions
    - Names/Definitions
- Infix and prefix functions
- Data Types in depth
  - Int, Integer
  - Float, Double
  - Rational
  - Bool
  - Char
  - Lists
  - Strings
  - Tuples + Tuples VS Lists
- Polymorphic values and type variables

### 3. Conditions and helper constructions [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F03-Conditions-and-helper-constructions.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=G0XPELNZuws)

- If-then-else
- Guards
- `let` expressions
- `where`
- Should I use `let` or `where`?
- Things to keep in mind

### 4. Pattern matching and Case [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F04-Pattern-matching.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=sQPGN4b95DU)

- What is pattern matching
- Pattern matching on
  - Function implementations
  - Lists
  - Tuples
- Case

### 5. Improving and combining functions [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F05-Improving-and-combining-functions.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/E-OEw4FKdf4)

- Higher-order functions
  - The `filter` function
  - The `any` function
- Lambda functions
- Precedence and associativity
- Curried functions
  - Partial application
- Composing and applying functions
  - The `$` operator
  - The `.` operator
- Point-free style

### 6. Recursion [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F06-Recursion-and-folds.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=wzvbUxSykXM)

- Why Recursion?
- Thinking Recursively
  - `sum` and `product`
- Steps to create your own recursive function
- Examples of recursion
  - `and`, `length`, `reverse`, `drop`, `take`, `map`, `filter`
- Extracting the `foldr` pattern
- The `foldl` function
- The `foldl'` function
- When to use `foldr`, `foldl`, and `foldl'`

### 7. Intro to Type Classes [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F07-Intro-to-Type-Classes.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=dGNd0GmsYWU)

- The awesomeness of type classes
- What are type classes
- Common type classes
  - `Eq`, `Ord`
  - `Num`, `Integral`, `Floating`
  - `Read`, `Show`
- The most general valid type
- Multiple constraints

### 8. Creating Non-Parameterized Types [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F08-Creating-non-parameterized-types.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=mAZC1w_VfEs)

- Type synonyms
  - How to define type synonyms
  - Why use type synonyms
- Defining new types
  - Creating new types with `data`
  - Using new types
  - Value parameters
- Record syntax

### 9. Creating Parameterized and Recursive Types [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F09-Creating-parameterized-and-recursive-types.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=wPV94aZIOGQ)

- Type Parameters
  - Prameteryzing `type` synonyms
  - Prameteryzing `data` types
- Recursive data types
  - `Tweet` me a river
  - A `Sequence` of `Node`s
  - A `Tree` of `Node`s
- Kinds
- The `newType` keyword

### 10. Creating Type Classes and Instances [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F10-Creating-Type-Classes-and-Instances.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=I6tmM3wNGEI)

- Overloading
- Steps to create Type Classes and Instances
- The `Eq` type class
  - Defining the Type Class
  - Defining multiple instances
  - Improving our `Eq` type class with mutual recursion (and Minimal Complete Definitions)
  - Defining an instance for a parameterized type.
- The `WeAccept` Type Class
- The `Container` Type Class
- Exploring `Ord` type class (Subclassing)
- Deriving
  - Deriving can go wrong

### 11. Basic IO

- We need side effects
- What is IO
- main + putStrLn + composing other functions
- `>>`
- `>>=`
- do notation
  - `do`
  - `<-`
  - `let`
- Some examples
- Read/Write to console
- Read/Write to file

### 12. Pragmas, Modules, and Cabal

- Prelude
- pragmas/extensions
- Overview of base modules
- Importing base modules
- A few modules
  - Data.Char
  - Data.Tuple
  - Data.Array
- Creating our own modules
- Cabal
  - What is it and why we use it
  - Cabal file
  - Using external libraries with Cabal

### 13. Bits and Bytes

- Grouping bits and bytes
- Haskell and bytes
- Lazy and strict byte strings
- Example

### 14. Handling Errors

- TODO

### 15. Learning on your own and Map

- Using GHCi to find out more
- Hoogle
- HaskellWiki
- Walking through while teaching Map module

---

### END OF THE BEGINNER SECTION 🐥

---

#### Congratulations! 🥳 You can call yourself a (beginner) Haskell programmer!

#### YOU'RE READY FOR THE MARLOWE PIONEER PROGRAM! 🥳🎉 (Keep going for Plutus.)

---

### START OF THE INTERMEDIATE SECTION 🐥⟶🐓

---

### 16. Monoid

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)

### 17. Functor

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)

### 18. Applicative

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)

### 19. Aeson

- Aeson

### 20. Monad

- Basic idea (definition without details)
- Intuitive examples
- Extracting the pattern
- Complete definition (with all the details/laws)
- `do` notation in general

### 21. Reader Monad

- Incentive/Motivation
- Binding strategy (see [here](https://wiki.haskell.org/All_About_Monads#The_Reader_monad))
- Definition
- Examples

### 22. Writer Monad

- Incentive/Motivation
- Binding strategy
- Definition
- Examples

### 23. State Monad

- Incentive/Motivation
- Binding strategy
- Definition
- Examples

### 24. Monadic functions / Operating with Monads

- liftM
- sequence and sequence\_
- mapM and mapM\_
- filterM
- foldM

### TODO: It keeps going, but I'm not sure about the outline yet. 😬
