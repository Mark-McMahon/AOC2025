class Day2:

    def parse_input(self):
        product_ranges = ""
        with open("input.txt", "r") as file:
            for line in file:
                product_ranges = line.split(",")
        return product_ranges

    def part1(self):
        product_ranges = self.parse_input()
        answer = 0
        for product_ranges in product_ranges:
            start_range, end_range = product_ranges.split("-")
            for i in range(int(start_range), int(end_range)+1):
                str_i = str(i)
                len_i = len(str_i)
                if len_i % 2 == 0:
                    mid_point = len_i // 2
                    if str_i[0:mid_point] == str_i[mid_point:]:
                        answer += i

        return answer

    def part2(self):
        product_ranges = self.parse_input()
        answer = 0
        for product_ranges in product_ranges:
            start_range, end_range = product_ranges.split("-")
            for i in range(int(start_range), int(end_range) + 1):
                str_i = str(i)
                len_i = len(str_i)
                is_invalid = False
                for j in range(2, len_i + 1):
                    if len_i % j == 0:
                        interval = len_i // j
                        list_parts = set()
                        for k in range(j):
                            # interval = 3
                            # [0*3]:[1*3] = [0]:[3]
                            # [1*3]:[2:3] = [3]:[6]

                            # interval = 2
                            # [0*2]:[1*2] = [0]:[2]
                            # [1*2]:[2:2] = [2]:[4]
                            # ...
                            interval_string = str_i[k*interval:(k+1)*interval]
                            list_parts.add(interval_string)
                        if len(list_parts) == 1:
                            answer += int(str_i)
                            is_invalid = True
                            break
                    if is_invalid:
                        break

        return answer

if __name__ == "__main__":
    day2 = Day2()
    print(day2.part1())
    print(day2.part2())
