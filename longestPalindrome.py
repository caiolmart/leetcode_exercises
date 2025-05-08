class Solution:
    def _is_palindrome(self, start, end, s):
        offset = 0
        while offset < (start - end) // 2:
            if s[start + offset] != s[end - offset]:
                return False
            offset += 1
        return True

    def longest_for_offset(self, s, s_inv, offset):
        if offset >= 0:
            this_s = s[offset:]
            this_s_inv = s_inv[:-offset] or s_inv # goes null for offset=0
        else:
            this_s = s[:offset]
            this_s_inv = s_inv[-offset:]
        comp_list = [a == b for a, b in  zip(this_s, this_s_inv)]
        if all(comp_list):
            return this_s

        for remove_n in range(1, len(comp_list)//2 + len(comp_list)%2):
            if all(comp_list[remove_n: -remove_n]):
                return this_s[remove_n: -remove_n]
        return ''

    def longestPalindrome(self, s: str) -> str:
        s_inv = s[::-1]
        longest = ''
        for offset in range(-len(s) + 1, len(s)):
            this_longest = self.longest_for_offset(s, s_inv, offset)
            if len(this_longest) > len(longest):
                longest = this_longest
            

        return longest


sol = Solution()
print(sol.longestPalindrome('cbbd'))
print(sol.longestPalindrome("ccd"))
print(sol.longestPalindrome('aacabdkacaa'))
print(sol.longestPalindrome("dtgrtoxuybwyfskikukcqlvprfipgaygawcqnfhpxoifwgpnzjfdnhpgmsoqzlpsaxmeswlhzdxoxobxysgmpkhcylvqlzenzhzhnakctrliyyngrquiuvhpcrnccapuuwrrdufwwungaevzkvwbkcietiqsxpvaaowrteqgkvovcoqumgrlsxvouaqzwaylehybqchsgpzbkfugujrostopwhtgrnrggocprnxwsecmvofawkkpjvcchtxixjtrnngrzqpiwywmnbdnjwqpmnifdiwzpmabosrmzhgdwgcgidmubywsnshcgcrawjvfiuxzyzxsbpfhzpfkjqcpfyynlpshzqectcnltfimkukopjzzmlfkwlgbzftsddnxrjootpdhjehaafudkkffmcnimnfzzjjlggzvqozcumjyazchjkspdlmifvsciqzgcbehqvrwjkusapzzxyiwxlcwpzvdsyqcfnguoidiiekwcjdvbxjvgwgcjcmjwbizhhcgirebhsplioytrgjqwrpwdciaeizxssedsylptffwhnedriqozvfcnsmxmdxdtflwjvrvmyausnzlrgcchmyrgvazjqmvttabnhffoe"))
print(sol.longestPalindrome("pihoigwlvzvtrugdolvtzrkyelaqdvbijzmkhebzawboaxkdjyfocpewwztffuaibcqurwwmijmvrnpfcoglyxpxkrbhupoxcafabxtoecodsjgngrionuvzaiigevuvruxxiwpjzjlqgenglhprcgzgpdzabrjhkbtfrbmwpcszepxhwiwdhvnpsmhhaiqsbeiwsaeomqtzcpjzfknejxlxwtpkufanhuoyjgihdzhtxnyctazzvnttjspfztjurdwmmzrvobcatkorfhpieoqfetcglembkgbexsznuduhrfoxkbswkanqwfkoktnnujqetijaqhrxuhkgsezfdrncbaltctwcourdbpdwhqlsxfwsoaduaqkbjeekwwykptjthhtokrvzsuelsywyznqscnwiszogzqvfsgggzltlvzkllinpfaigswquqfvabbzvestwxhbnfjhnvfhyxalchmtkcwnyyrbwjsoqooypwteozbivqiyldpqlykxinmzkgnmfbobgjivlzubfen"))


