"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Nelson Rainey.
"""  # DOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DOne: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()


    # -------------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    go_forward_button = ttk.Button(frame1, text='Forward')
    go_forward_button.grid()

    # -------------------------------------------------------------------------
    # DOne: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DOne: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    go_forward_button['command'] = (lambda:print('hello'))
    # -------------------------------------------------------------------------
    # DOne: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    new_entry = ttk.Entry(frame1)
    new_entry.grid()

    new_button = ttk.Button(frame1, text = 'new_button')
    new_button.grid()

    second_entry = ttk.Entry(frame1)
    second_entry.grid()

    third_button = ttk.Button(frame1,text = 'third_button')
    third_button.grid()

    new_button['command'] = (lambda:my_contents(new_entry,second_entry))

    def my_contents(stuff,n):
        contents_of_entry_box = stuff.get()
        number = n.get()
        if contents_of_entry_box == 'ok':
            for k in range(int(number)):
                print('Hello')
            return
        for j in range (int(number)):
            print('goodbye')
    # -------------------------------------------------------------------------
    # DOne: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------


    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DOne: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

    root.mainloop()
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
