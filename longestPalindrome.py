class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palindrome_matrix = [
            [i == j for i in range(len(s))] for j in range(len(s))
        ]
        best_pos = (0, 0)

        # parallel diagonal
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                is_palindrome_matrix[i][i + 1] = True
                best_pos = (i, i + 1)

        for offset in range(2, len(s)):
            for i in range(0, len(s) - offset):
                if (
                    is_palindrome_matrix[i + 1][i + offset - 1]
                    and s[i] == s[i + offset]
                ):
                    is_palindrome_matrix[i][i + offset] = True
                    best_pos = (i, i + offset)

        return s[best_pos[0] : best_pos[1] + 1]


sol = Solution()
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("ccd"))
print(sol.longestPalindrome("aacabdkacaa"))
print(
    sol.longestPalindrome(
        "dtgrtoxuybwyfskikukcqlvprfipgaygawcqnfhpxoifwgpnzjfdnhpgmsoqzlpsaxmeswlhzdxoxobxysgmpkhcylvqlzenzhzhnakctrliyyngrquiuvhpcrnccapuuwrrdufwwungaevzkvwbkcietiqsxpvaaowrteqgkvovcoqumgrlsxvouaqzwaylehybqchsgpzbkfugujrostopwhtgrnrggocprnxwsecmvofawkkpjvcchtxixjtrnngrzqpiwywmnbdnjwqpmnifdiwzpmabosrmzhgdwgcgidmubywsnshcgcrawjvfiuxzyzxsbpfhzpfkjqcpfyynlpshzqectcnltfimkukopjzzmlfkwlgbzftsddnxrjootpdhjehaafudkkffmcnimnfzzjjlggzvqozcumjyazchjkspdlmifvsciqzgcbehqvrwjkusapzzxyiwxlcwpzvdsyqcfnguoidiiekwcjdvbxjvgwgcjcmjwbizhhcgirebhsplioytrgjqwrpwdciaeizxssedsylptffwhnedriqozvfcnsmxmdxdtflwjvrvmyausnzlrgcchmyrgvazjqmvttabnhffoe"
    )
)
print(
    sol.longestPalindrome(
        "pihoigwlvzvtrugdolvtzrkyelaqdvbijzmkhebzawboaxkdjyfocpewwztffuaibcqurwwmijmvrnpfcoglyxpxkrbhupoxcafabxtoecodsjgngrionuvzaiigevuvruxxiwpjzjlqgenglhprcgzgpdzabrjhkbtfrbmwpcszepxhwiwdhvnpsmhhaiqsbeiwsaeomqtzcpjzfknejxlxwtpkufanhuoyjgihdzhtxnyctazzvnttjspfztjurdwmmzrvobcatkorfhpieoqfetcglembkgbexsznuduhrfoxkbswkanqwfkoktnnujqetijaqhrxuhkgsezfdrncbaltctwcourdbpdwhqlsxfwsoaduaqkbjeekwwykptjthhtokrvzsuelsywyznqscnwiszogzqvfsgggzltlvzkllinpfaigswquqfvabbzvestwxhbnfjhnvfhyxalchmtkcwnyyrbwjsoqooypwteozbivqiyldpqlykxinmzkgnmfbobgjivlzubfen"
    )
)
