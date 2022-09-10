# share-reference
Share reference will be checked when we use `is` statement for 2 variable. in this example `int` type.
Its so intresting when two variables have two equal values, like:
```
a = 0
b = 0
```
When we check equality of those variables using `is` it's return `True`:
```
a is b
True
```
But that is the interest part, its `True` when `variable < 257`:
```
a = 256
b = 256

a is b
True

a = 257
b = 257

a is b
False
```
`variable >= 257` all return `False` in equality check:
```
a = 258
b = 258
a is b
False

a = 19324
b = 19324
a is b
False
```
you can see the loop that show you proof in `main.py`
