class ContestResult:
    winner = ""
    second_place = ""
    third_place = ""

    def set_winner(self, winner):
        self.winner = winner

    def set_second_place(self, second_winner):
        self.second_place = second_winner

    def set_third_place(self, third_winner):
        self.third_place = third_winner

    def get_winner(self):
        return self.winner

    def get_sec_winner(self):
        return self.second_place

    def get_third_winner(self):
        return self.third_place

example_contest_result = ContestResult()
example_contest_result.set_winner("AMM")
example_contest_result.set_second_place("HIGK")
example_contest_result.set_third_place("NMKK")

print("Winner: ", example_contest_result.get_winner())
print("Second Winner: ", example_contest_result.get_sec_winner())
print("Third Winner: ", example_contest_result.get_third_winner())
