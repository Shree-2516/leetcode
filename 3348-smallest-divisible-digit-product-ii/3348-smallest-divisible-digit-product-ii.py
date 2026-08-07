class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        k_factor_counts = {
            0: {},
            1: {},
            2: {2: 1},
            3: {3: 1},
            4: {2: 2},
            5: {5: 1},
            6: {2: 1, 3: 1},
            7: {7: 1},
            8: {2: 3},
            9: {3: 2},
        }

        def get_prime_count_t(val):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in [2, 3, 5, 7]:
                while val % p == 0:
                    val //= p
                    count[p] += 1
            return count, val == 1

        prime_count, is_divisible = get_prime_count_t(t)
        if not is_divisible:
            return "-1"

        def get_factor_count(count):
            c2, c3, c5, c7 = count.get(2, 0), count.get(3, 0), count.get(5, 0), count.get(7, 0)
            c8 = c2 // 3
            rem2 = c2 % 3
            c9 = c3 // 2
            rem3 = c3 % 2
            c4 = rem2 // 2
            rem2 %= 2
            c6 = 0
            if rem2 == 1 and rem3 == 1:
                rem2 = 0
                rem3 = 0
                c6 = 1
            if rem3 == 1 and c4 == 1:
                rem2 = 1
                c6 = 1
                rem3 = 0
                c4 = 0
            return {2: rem2, 3: rem3, 4: c4, 5: c5, 6: c6, 7: c7, 8: c8, 9: c9}

        def sum_values(fc):
            return sum(fc.values())

        def construct(fc):
            res = []
            for d in [2, 3, 4, 5, 6, 7, 8, 9]:
                res.append(str(d) * fc.get(d, 0))
            return "".join(res)

        factor_count = get_factor_count(prime_count)
        if sum_values(factor_count) > len(num):
            return construct(factor_count)

        def subtract(a, b):
            return {k: max(0, a.get(k, 0) - b.get(k, 0)) for k in set(a) | set(b)}

        def get_string_prime_count(s):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for char in s:
                d = int(char)
                if d in k_factor_counts:
                    for p, f in k_factor_counts[d].items():
                        count[p] += f
            return count

        prime_count_prefix = get_string_prime_count(num)
        first_zero_index = num.find('0')
        if first_zero_index == -1:
            first_zero_index = len(num)
            def is_subset(a, b):
                return all(b.get(k, 0) >= a.get(k, 0) for k in a)
            if is_subset(prime_count, prime_count_prefix):
                return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            for p, f in k_factor_counts[d].items():
                prime_count_prefix[p] -= f

            space_after_this_digit = len(num) - 1 - i
            if i > first_zero_index:
                continue

            for bigger_digit in range(d + 1, 10):
                rem_needed = subtract(
                    subtract(prime_count, prime_count_prefix),
                    k_factor_counts[bigger_digit]
                )
                factors_after_replacement = get_factor_count(rem_needed)
                if sum_values(factors_after_replacement) <= space_after_this_digit:
                    fill_ones = space_after_this_digit - sum_values(factors_after_replacement)
                    return num[:i] + str(bigger_digit) + "1" * fill_ones + construct(factors_after_replacement)

        factors_after_extension = get_factor_count(prime_count)
        return "1" * (len(num) + 1 - sum_values(factors_after_extension)) + construct(factors_after_extension)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna