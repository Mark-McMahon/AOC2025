
class Day1:

    CURR_POINTER = 50
    LOW = 0
    HIGH = 99

    answer = 0
    answer2 = 0

    def part1(self):
        with open("input.txt", "r") as file:
            for line in file:
                rotation = int(line[1:])
                if line[0] == "L":
                    self.CURR_POINTER = (self.CURR_POINTER - rotation) % 100
                else:
                    self.CURR_POINTER = (self.CURR_POINTER + rotation) % 100

                if self.CURR_POINTER == 0:
                    self.answer += 1

        return self.answer


    def part2(self):
        self.CURR_POINTER = 50
        with open("input.txt", "r") as file:
            for line in file:
                direction = line[0]
                distance = int(line[1:])

                if direction == 'L':
                    if self.CURR_POINTER == 0:
                        self.answer2 += distance // 100
                    else:
                        if distance >= self.CURR_POINTER:
                            self.answer2 += 1 + (distance - self.CURR_POINTER) // 100
                    self.CURR_POINTER = (self.CURR_POINTER - distance) % 100
                else:
                    if self.CURR_POINTER == 0:
                        self.answer2 += distance // 100
                    else:
                        distance_to_zero = 100 - self.CURR_POINTER
                        if distance >= distance_to_zero:
                            self.answer2 += 1 + (distance - distance_to_zero) // 100
                    self.CURR_POINTER = (self.CURR_POINTER + distance) % 100

        return self.answer2

if __name__ == "__main__":
    day1 = Day1()
    answer = day1.part1()
    answer2 = day1.part2()

    print(answer)
    print(answer2)

