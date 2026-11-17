
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in seen:
                seen[key] = []

            seen[key].append(word)

        return list(seen.values())
