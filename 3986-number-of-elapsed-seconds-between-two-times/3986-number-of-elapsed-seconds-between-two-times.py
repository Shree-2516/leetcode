class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def to_seconds(time_str: str) -> int:
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m *60 + s
        start_seconds = to_seconds(startTime)
        end_seconds = to_seconds(endTime)

        return end_seconds - start_seconds

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna