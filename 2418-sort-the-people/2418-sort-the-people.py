class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = list(zip(names,heights))
        lst.sort(key = lambda x: x[1], reverse = True)
        return [x[0] for x in lst]