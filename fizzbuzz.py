class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        response = []
        for i in range(1, A+1):
            if i % 3 == 0 and i % 5 == 0: response.append("FizzBuzz")
            elif i % 3 == 0: response.append("Fizz")
            elif i % 5 == 0: response.append("Buzz")
            else: response.append(str(i))
        
        return " ".join(response)

if __name__ == "__main__":
    print(Solution().fizzBuzz(5))

