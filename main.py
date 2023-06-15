class Solution:    
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        subtractive_cases = {
            'IV': 4, 'IX': 9, 'XL': 40,
            'XC': 90, 'CD': 400, 'CM': 900
        }
        
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in subtractive_cases:
                total += subtractive_cases[s[i:i+2]]
                i += 2
            else:
                total += roman_values[s[i]]
                i += 1

        return total


solution = Solution()

# Call the romanToInt method and pass a Roman numeral string
roman_numeral = "MCMXCIV"
result = solution.romanToInt(roman_numeral)

# Print the result
print(f"The integer representation of {roman_numeral} is: {result}")
