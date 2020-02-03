class Branch:

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.time_length = 0
        self.completion = "todo"
        self.completion_states = ("to do", "In progress", "completed",)
        self.subbranches = []
        self.subbranch_id = 0
        self.subbranches_length = self.calculate_subbranches()

    def rename(self):
        """Change the name of the branch"""
        self.name = input("Enter new name for the leaf")
        return self.name

    def add_description(self):
        """ aAdd notes here to previous notes"""
        self.description = self.description + input("You can add a description ")
        return self.description

    def delete_description(self):
        """If you dont like what you have written before"""
        self.description = ""
        return self.description

    def set_time_length(self):
        """Set the time spend on work with this leaf"""
        self.time_length = int(input("How long you are doing this task(in hours)"))
        return self.time_length

    def change_completion_state(self):
        """ choose the state of completion"""
        while True:
            choice = input("""
            choose 0 to  change the state on  'to do'
            choose 1 to  change the state on  'In progress' 
            choose 2 to  change the state on  'completed"'
            """)
            if choice == "0":
                self.completion = self.completion_states[0]
                return self.completion
            elif choice == "1":
                self.completion = self.completion_states[1]
                return self.completion
            elif choice == "2":
                self.completion = self.completion_states[2]
                return self.completion

    def create_subbranch(self):
        """Create a new subbranch which id will be 1 more then before """
        subbranch_name = input("select a name for the subbranch")
        branch = Branch(subbranch_name)
        self.subbranch_id += 1
        self.subbranches.append(branch)
        return self.subbranch_id

    def calculate_subbranches(self):
        """calculates whole amount of time the subbranches have"""
        whole_time = 0
        for i in self.subbranches:
            whole_time += i.timelength
        self.subbranches_length = whole_time
        return self.subbranches_length

    def show_all_subbranches(self):
        for i in self.subbranches:
            print(i)
            if i.subbranches == []:
                pass
            else:
                i.show_all_subbranches()

    def __str__(self):
        return f"""
        This the {str(self.name)}
        Description : {self.description} 
        Length: {self.time_length} 
        State of completion: {self.completion}
        self.subbranch_id: {self.subbranch_id}
        ********************************* """


