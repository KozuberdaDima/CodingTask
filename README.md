This program implements the logic that translates stringify integer values into a numeric format.

Conditions:
1) Empty string is not applicable.
2) Length of the input string: 2 ≤ |s| ≤ 2^32-1.
3) String should contain positive or negative numeric values in stringified format from the range [0-9] and arithmetical operation signs [‘+’, ‘-’] before the numeric value.
4) Decimal values are not applicable.

Sample: “123345” -> 123345, “-123345” -> -123345, “+1” -> 1.