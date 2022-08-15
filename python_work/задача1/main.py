
import numexpr

expr = input("Введите математическое выражение: ")
result = numexpr.evaluate(expr)

print(result)

