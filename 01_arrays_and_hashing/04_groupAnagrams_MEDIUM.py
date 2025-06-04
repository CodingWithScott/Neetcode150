class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ASCII_OFFSET = 97 
        anagrams = {}
        # For all words, count chars and build dictionary
        # key: char count, value = list of anagrams
        for curr_word in strs:
            curr_char_count = [0]*26
            # Count total chars in each word
            for curr_char in curr_word:
                curr_char_count[ord(curr_char)-ASCII_OFFSET] += 1
            
            if (anagrams.get(tuple(curr_char_count))):  
                anagrams[tuple(curr_char_count)].append(curr_word)
            else:
                anagrams[tuple(curr_char_count)] = [curr_word]
            
        # Iterate over all keys and print groupings
        output = []
        for key in anagrams:
            value = anagrams[key]
            output.append(value)

        return output

sol = Solution()       
        
strs1 = ["act","pots","tops","cat","stop","hat"]
valid_output1 = [["hat"],["act", "cat"],["stop", "pots", "tops"]]
output1 = sol.groupAnagrams(strs1)

strs2 = ["x"]
valid_output2 = [["x"]]
output2 = sol.groupAnagrams(strs2)

strs3 = [""]
valid_output3 = [[""]]
output3 = sol.groupAnagrams(strs3)


if (output1 == valid_output1):
    print('Example 1 passed')
else:
    print('Example 1 failed')
    print(f'Expected: {valid_output1}')
    print(f'Actual: {output1}')

if (output2 == valid_output2):
    print('Example 2 passed')
else:
    print('Example 2 failed')
    print(f'Expected: {valid_output2}')
    print(f'Actual: {output2}')

if (output3 == valid_output3):
    print('Example 3 passed')
else:
    print('Example 3 failed')
    print(f'Expected: {valid_output3}')
    print(f'Actual: {output3}')

