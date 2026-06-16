def is_safe(report):
    diffs = [b - a for a, b in zip(report, report[1:])]

    return (
        all(1 <= abs(d) <= 3 for d in diffs)
        and (
            all(d > 0 for d in diffs)
            or all(d < 0 for d in diffs)
        )
    )


def can_be_safe(report):
    return any(
        is_safe(report[:i] + report[i + 1:])
        for i in range(len(report))
    )


def load_data(filename):
    with open(filename) as f:
        return [
            list(map(int, line.split()))
            for line in f
            if line.strip()
        ]


data = load_data("input.txt")

part1 = sum(is_safe(report) for report in data)

part2 = sum(
    is_safe(report) or can_be_safe(report)
    for report in data
)

print("Part 1:", part1)
print("Part 2:", part2)