## Files
### man
Manual for a command

### ls
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

      -a, --all                  do not ignore entries starting with .
      -l use a long listing format
      -o                         like -l, but do not list group information
      -m fill width with a comma separated list of entries
      -r, --reverse              reverse order while sorting
      -R, --recursive            list subdirectories recursively
      -S                         sort by file size, largest first
          --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                                   time (-t), version (-v), extension (-X)
          --time=WORD            with -l, show time as WORD instead of default
                                   modification time: atime or access or use (-u);
                                   ctime or status (-c); also use specified time
                                   as sort key if --sort=time (newest first)
          --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
      -t                         sort by modification time, newest first

      -1                         list one file per line.  Avoid '\n' with -q or -b

### apropos "search key words"
To search a command for action when you don't know the sepcific command

# Files & Folders:

## file "file_name" : file type
    ```shell script
    harryduong@harry-ubuntu:~$ file PERSONAL_PROJECTS/code_reference/README.md 
    PERSONAL_PROJECTS/code_reference/README.md: ASCII text```

## stat "file_name" :
    ```shell script
    harryduong@harry-ubuntu:~$ stat PERSONAL_PROJECTS/code_reference/Machine\ Learning\ Notebook.ipynb 
      File: PERSONAL_PROJECTS/code_reference/Machine Learning Notebook.ipynb
      Size: 692       	Blocks: 8          IO Block: 4096   regular file
    Device: 805h/2053d	Inode: 1073831     Links: 1
    Access: (0664/-rw-rw-r--)  Uid: ( 1000/harryduong)   Gid: ( 1000/harryduong)
    Access: 2020-11-27 17:00:07.846683872 +1100
    Modify: 2020-11-27 16:59:35.354684274 +1100
    Change: 2020-11-27 16:59:35.354684274 +1100
    Birth: -
    ```
## cd: Change directory
    ```shell script
    cd .. : back to parent folder
    cd    : back to root folder
    cd -  : switch to previous used folder
    ```

## pwd: current working directory

## mkdir
Make directory. Can include multiple folder name separated by space.

```shell script
  -p, --parents     no error if existing, make parent directories as needed

```

```shell script
harryduong@harry-ubuntu:~$ mkdir -p testing/making_new_folder/sub_folder
harryduong@harry-ubuntu:~$ ls
Default.xml  DEVELOPMENT  Downloads      jaas.conf  Music              Pictures            Public            snap       testing  watchers.xml
Desktop      Documents    first_project  krb5.conf  PERSONAL_PROJECTS  psql_database_conn  pycharm-2020.2.3  Templates  Videos
harryduong@harry-ubuntu:~$ ls -R testing/
testing/:
making_new_folder

testing/making_new_folder:
sub_folder

testing/making_new_folder/sub_folder:
```
## rmdir
remove folder, but folder must be empty

## cp <source_file> <destination>
Copy file

## mv <source_file> <destination>
Move file or rename file.
Widcard (*,?) can be use:
```shell script
mv *.txt new_folder/
```

## rm
remove files:
```shell script
rm -r folder_name/ : remove all files and folder under this path. Note the / 

```

## Terminal Shortcut:
| **Shortcut**      | **Action**                                      
| ------------------| -------------------------------------------
| Ctrl A            | Move to beginning of the line
| Ctrl E            | Move to end of the line
| Ctrl Left Arrow   | move backward one word
| Ctrl Right Arrow  | move forward one word
| Ctrl U            | Remove from cursor to beginning of the line
| Ctrl K            | Remove from cursor to end of the line
| Ctrl Y            | Paste cropped text
| Ctrl Shift C      | Copy to Clipboard
| Ctrl Shift V      | Paste from clipboard
| Up & Down arrow   | Show previous/last command
| Ctrl R            | Search Command History (press again to continue searching)
| Ctrl C            | Cancel a command
