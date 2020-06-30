'''
Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

Inputs

- Original list of strings

- List of strings to be added

- List of strings to be removed

Return

- List shall only contain unique values

- List shall be ordered as follows

--- Most character count to least character count

--- In the event of a tie, reverse alphabetical

Other Notes

- You can use any programming language you like

- The function you submit shall be runnable

For example:

Original List = ['one', 'two', 'three',]

Add List = ['one', 'two', 'five', 'six]

Delete List = ['two', 'five']

Result List = ['three', 'six', 'one']*

'''

def merge_lists(start_list,add_list,del_list):
    
    set_start = set(start_list)
    set_add = set(add_list)
    set_del = set(del_list)
   
    set_final = (set_start | set_add) - set_del

   
    final_list = list(set_final)
    
    final_list.sort(key=len, reverse=True)

    return final_list

def main():

    start_list = ['one', 'two', 'three',]
    
    add_list = ['one', 'two', 'five', 'six']

    del_list = ['two', 'five']

    #final_list = ['three', 'six', 'one']
                  
    final_list = merge_lists(start_list,add_list,del_list)
                
    print(final_list)
    
main()