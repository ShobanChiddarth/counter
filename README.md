# counter
Simple python file that counts number of times it was run.

It counts and stores the value in a binary file 'counterfile.bin'

### Programming Logic used
1. If 'counterfile.bin' (the file which the count value is stored) exists,
   open it (with file-handle as `counterfile`) and pickle.load it to read 
   the binary value stored in it.
2. Else -> create a file 'counterfile.bin' (with file-handle `counterfile`)
           create a variable `count` (with value 0)
           dump the variable in the file (pickle.dump)
3. Now, close the file (file-handle `counterfile`)
        (So that the file is closed anyways)
4. Increment the variable `count` (+1)
5. Delete the file 'counterfile.bin'
6. Create a new file and dump `count` in it
7. Close the file handle
8. Finally, print the variable `count`