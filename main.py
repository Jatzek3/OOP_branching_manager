from branches import Branch


def Menu(branch):
    while True:
        print("""
        Press 1 and enter to create new subbranch
        Press 2 and enter to rename this branch
        Press 3 and enter to add description
        Press 4 and enter to delete description
        Press 5 and enter to set time length(in hours) for branch
        Press 6 and enter to change the state of completion
        Press 7 and enter to show all subbranches
        
        Press 9 to inspect this branch
        """)
        choice = int(input(">>>"))
        if choice == 1:
            branch.create_subbranch()
        elif choice == 2:
            branch.rename()
        elif choice == 3:
            branch.add_description()
        elif choice == 4:
            branch.delete_description()
        elif choice == 5:
            branch.set_time_length()
        elif choice == 6:
            branch.change_completion_state()
        elif choice == 7:
            branch.show_all_subbranches()
        elif choice == 9:
            print(branch)


branch1 = Branch("starting")
Menu(branch1)
