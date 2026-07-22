from dataclasses import dataclass
import itertools
from typing import List


@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums: List[int]):
        self.n = len(nums)

        if self.n == 0:
            self.st = [[0]]
            return

        self.st = [[0] * self.n for _ in range(self.n.bit_length())]
        self.st[0] = nums[:]

        k = 1
        while (1 << k) <= self.n:
            length = 1 << k
            half = length >> 1

            for i in range(self.n - length + 1):
                self.st[k][i] = max(
                    self.st[k - 1][i],
                    self.st[k - 1][i + half]
                )

            k += 1

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0

        p = (r - l + 1).bit_length() - 1
        return max(
            self.st[p][l],
            self.st[p][r - (1 << p) + 1]
        )


class Solution:
    def maxActiveSectionsAfterTrade(
        self,
        s: str,
        queries: List[List[int]]
    ) -> List[int]:

        ones = s.count('1')

        zero_groups, zero_group_index = self._get_zero_groups(s)

        if not zero_groups:
            return [ones] * len(queries)

        merge_lengths = self._get_merge_lengths(zero_groups)
        st = SparseTable(merge_lengths)

        ans = []

        for l, r in queries:

            left = (
                -1
                if zero_group_index[l] == -1
                else zero_groups[zero_group_index[l]].length
                - (l - zero_groups[zero_group_index[l]].start)
            )

            right = (
                -1
                if zero_group_index[r] == -1
                else r - zero_groups[zero_group_index[r]].start + 1
            )

            start_group = zero_group_index[l] + 1

            end_group = (
                zero_group_index[r]
                if s[r] == '1'
                else zero_group_index[r] - 1
            )

            start_adj = start_group
            end_adj = end_group - 1

            best = ones

            if (
                s[l] == '0'
                and s[r] == '0'
                and zero_group_index[l] + 1 == zero_group_index[r]
            ):
                best = max(best, ones + left + right)

            elif start_adj <= end_adj:
                best = max(best, ones + st.query(start_adj, end_adj))

            if (
                s[l] == '0'
                and zero_group_index[l] + 1
                <= (
                    zero_group_index[r]
                    if s[r] == '1'
                    else zero_group_index[r] - 1
                )
            ):
                best = max(
                    best,
                    ones + left + zero_groups[zero_group_index[l] + 1].length
                )

            # Right boundary zero group is partial.
            if (
                s[r] == '0'
                and zero_group_index[l] < zero_group_index[r] - 1
            ):
                best = max(
                    best,
                    ones + right + zero_groups[zero_group_index[r] - 1].length
                )

            ans.append(best)

        return ans

    def _get_zero_groups(
        self,
        s: str
    ) -> tuple[List[Group], List[int]]:

        groups = []
        group_index = []

        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))

            group_index.append(len(groups) - 1)

        return groups, group_index

    def _get_merge_lengths(
        self,
        groups: List[Group]
    ) -> List[int]:

        return [
            a.length + b.length
            for a, b in itertools.pairwise(groups)
        ]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna