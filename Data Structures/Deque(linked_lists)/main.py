"""Main File"""
from collections import deque
from song import Song

def main():

    playlist = deque()

    options = 0

    while options != 4:

        print("Options: ")
        print("1. Add a new song to the end of the playlist.")
        print("2. Insert a new song to the beginning of the playlist.")
        print("3. Play the next song.")
        print("4. Quit.")

        options = int(input("Enter selection: "))
        print()

        if options == 1:

            s = Song()
            s.prompt()
            playlist.append(s)
        
        elif options == 2:

            s = Song()
            s.prompt()
            playlist.appendleft(s)
        
        elif options == 3:
            
            if len(playlist) == 0:
                print("The playlist is currently empty.")

            else:
                s.display()
        print()
    



if __name__ == "__main__":
    main()