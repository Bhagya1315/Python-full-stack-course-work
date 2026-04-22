'''class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1


class Voter:
    def __init__(self, voter_id):
        self.voter_id = voter_id
        self.has_voted = False


class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = {}

    def add_candidate(self, name):
        candidate = Candidate(name)
        self.candidates.append(candidate)

    def register_voter(self, voter_id):
        if voter_id not in self.voters:
            self.voters[voter_id] = Voter(voter_id)
        else:
            print("Voter already registered!")

    def show_candidates(self):
        print("\nCandidates:")
        for i, candidate in enumerate(self.candidates):
            print(f"{i + 1}. {candidate.name}")

    def vote(self, voter_id, candidate_index):
        if voter_id not in self.voters:
            print("Voter not registered!")
            return

        voter = self.voters[voter_id]

        if voter.has_voted:
            print("You have already voted!")
            return

        if candidate_index < 0 or candidate_index >= len(self.candidates):
            print("Invalid candidate!")
            return

        self.candidates[candidate_index].add_vote()
        voter.has_voted = True
        print("Vote cast successfully!")

    def show_results(self):
        print("\nVoting Results:")
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")


# ------------------ MAIN PROGRAM ------------------

vs = VotingSystem()

# Add candidates
vs.add_candidate("Alice")
vs.add_candidate("Bob")
vs.add_candidate("Charlie")

# Register voters
vs.register_voter("V1")
vs.register_voter("V2")
vs.register_voter("V3")

# Voting process
while True:
    print("\n1. Show Candidates")
    print("2. Vote")
    print("3. Show Results")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        vs.show_candidates()

    elif choice == '2':
        voter_id = input("Enter your Voter ID: ")
        vs.show_candidates()
        try:
            candidate_choice = int(input("Enter candidate number: ")) - 1
            vs.vote(voter_id, candidate_choice)
        except ValueError:
            print("Invalid input!")

    elif choice == '3':
        vs.show_results()

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
'''





class Event:
    def __init__(self,event_name):
        self.event_name = eventname

class farewell:
    def __init__(self,people):
        print("People need to be share their opnionn about seniors")

class common:
    def __init__(self):
        #print("Come with a traditional manner")
        print("Enjoying the event")

class pooja(common):
    def __init__(self):
        print("Come with a traditional manner")
        print("Participate and getting blessed from god")

class dance:
    def __init__(self):
        print("Wear dance costumtions only")


ce = Event('farewell')
ce1 = farewell()
ce1.farewell("2026")
