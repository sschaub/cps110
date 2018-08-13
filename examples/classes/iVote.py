class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __repr__(self):
        return self.name + ":" + str(self.votes)

    def castVote(self):
        self.votes += 1

class Race:
    def __init__(self, office: str, candidates):
        self.office = office
        self.candidates = candidates

    def voteFor(self, candidateName: str):
        for candidate in self.candidates:
            if candidate.name == candidateName:
                candidate.castVote()
 
candidates = [Candidate('Mr. Trump'), Candidate('Mrs. Clinton')]

print(candidates)
candidates[0].castVote()

presRace = Race('President of the United States', candidates)
presRace.voteFor('Mrs. Clinton')
print(candidates)