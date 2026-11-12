class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for s in strs:
            string = "".join(sorted(s))
            if string not in result:
                result[string] = []

            result[string].append(s)

        return list(result.values())
