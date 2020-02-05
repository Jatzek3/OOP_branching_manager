from branches import Branch

dir_stack =[]


def go_to_upper_branch():
    if dir_stack != []:
        return menu(dir_stack.pop())
    else:
        pass


def choose_subbranch(branch_entering):
    """choose a branch to work with"""
    selected_id = int(input("enter id of branch to work with"))
    dir_stack.append(branch_entering)
    return menu(branch_entering.subbranches[selected_id])


def menu(branch):

    while True:
        print("""
        Press 1 and enter to create new subbranch
        Press 2 and enter to rename this branch
        Press 3 and enter to add description
        Press 4 and enter to delete description
        Press 5 and enter to set time length(in hours) for branch
        Press 6 and enter to change the state of completion
        Press 7 and enter to show all subbranches
        Press 8 and enter to choose a subbranch
        Press 9 and enter to inspect this branch
        Press 10 and enter to go to the upper branch
        Press 11 and enter to quit
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
        elif choice == 8:
            choose_subbranch(branch)
        elif choice == 9:
            print(branch)
        elif choice == 10:
            go_to_upper_branch()
        elif choice == 11:
            quit()


branch1 = Branch("starting")
menu(branch1)
