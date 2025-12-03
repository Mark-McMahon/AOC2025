class Day3:
    def parseInput(self):
        banks = []
        with open("input.txt", "r") as file:
            for line in file:
                banks.append(line.strip())
        return banks


    def part1(self):
        banks = self.parseInput()
        answer = 0

        for bank in banks:
            bank_max = 0
            for i in range(len(bank)):
                for j in range(i + 1, len(bank)):
                    bank_max = max(bank_max, int(bank[i] + bank[j]))

            answer += bank_max

        return answer

    def part2(self):
        banks = self.parseInput()
        answer = 0
        for bank in banks:
            start = 0
            bank_max = []
            for i in range(12):
                nums_left =  12 - (i+1)
                end = len(bank) - nums_left

                window = (bank[start:end])
                max_num = max(window)

                bank_max.append(max_num)

                idx = window.index(max_num)
                start += idx + 1

            answer += int(''.join(bank_max))

        return answer


if __name__ == "__main__":
    day3 = Day3()
    print(day3.part1())
    print(day3.part2())


