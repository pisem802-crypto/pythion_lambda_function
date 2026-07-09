# Python Lambda Interview Questions & Answers

# Beginner

## What is a lambda function?

A lambda function is a small anonymous function created using the
`lambda` keyword. It can accept any number of arguments but contains
only **one expression**, whose value is returned automatically.

**Example**

``` python
square = lambda x: x * x
print(square(5))  # 25
```

## Why are lambda functions called anonymous functions?

They are called anonymous because they do not need a name.

``` python
print((lambda x: x+1)(5))  # 6
```

## What is the syntax of a lambda function?

``` python
lambda arguments: expression
```

Example:

``` python
add = lambda a,b: a+b
print(add(2,3))
```

## How is lambda different from a regular function?

  Regular Function           Lambda
  -------------------------- ---------------------------
  Uses `def`                 Uses `lambda`
  Multiple statements        Single expression
  Explicit `return`          Implicit return
  Better for complex logic   Best for short operations

## Can lambda functions contain multiple expressions?

No. A lambda can contain only one expression.

# Intermediate

## How does map() work with lambda?

`map()` applies a function to every element.

``` python
nums=[1,2,3]
print(list(map(lambda x:x*x, nums)))
```

## How does filter() use lambda?

`filter()` keeps elements where the lambda returns `True`.

``` python
nums=[1,2,3,4]
print(list(filter(lambda x:x%2==0, nums)))
```

## What is reduce()?

`reduce()` repeatedly combines elements into a single value.

``` python
from functools import reduce
print(reduce(lambda a,b:a+b,[1,2,3,4]))
```

## How do you sort using lambda?

``` python
employees=[("John",50000),("Alice",70000)]
print(sorted(employees,key=lambda x:x[1]))
```

## When should lambda functions be avoided?

-   Complex business logic
-   Multiple statements
-   Error handling
-   Poor readability

## What are the limitations of lambda functions?

-   One expression only
-   No statements like loops/try-except
-   Harder to debug
-   Less readable for complex code

# Advanced

## When would you choose a regular function over lambda?

Choose `def` when logic is complex, reused, documented, or tested.

## How do lambda functions improve ETL pipelines?

They simplify inline transformations.

``` python
records=[{"salary":50000},{"salary":60000}]
updated=list(map(lambda r:{**r,"bonus":r["salary"]*0.1},records))
print(updated)
```

## How are lambda functions used in Pandas?

``` python
import pandas as pd
df=pd.DataFrame({"salary":[50000,60000]})
df["bonus"]=df["salary"].apply(lambda s:s*0.1)
```

## How do lambda expressions improve sorting performance?

They avoid defining a separate helper function and are commonly used as
lightweight key functions. The main performance benefit in sorting comes
from Python's efficient `key=` mechanism, not from lambda itself.

## Can lambda functions capture variables from enclosing scopes?

Yes, through closures.

``` python
factor=10
multiply=lambda x:x*factor
print(multiply(5))
```

## What are common mistakes while using lambda expressions?

-   Writing complex expressions
-   Using lambda where `def` is clearer
-   Forgetting `filter()` needs a boolean
-   Overusing nested lambdas
-   Assuming lambda is always faster than regular functions (it is not)

# Interview Tips

-   Prefer lambda for `map()`, `filter()`, `sorted()`, `reduce()`, and
    simple callbacks.
-   Prefer `def` for production business logic and reusable code.
