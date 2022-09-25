class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = dict.fromkeys((3, 6, 9, 12), "Fizz")
        buzz = dict.fromkeys((5, 10), "Buzz")
        fizz_buzz_dict = {0: "FizzBuzz", **fizz, **buzz}
		
        return [fizz_buzz_dict.get(n % 15, str(n)) for n in range(1, n+1)]
    
