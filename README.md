# counter
Simple python file that counts number of times it was run.



It counts and stores the value in a binary file 'counterfile.bin'

### The Algorithm used
1. If 'counterfile.bin' (the file which the count value is stored) exists,
   open it (with file-handle as `counterfile`) and pickle.load it to read 
   the binary value stored in it.
1. Else -> create a file 'counterfile.bin' (with file-handle `counterfile`)
           create a variable `count` (with value 0)
           dump the variable in the file (pickle.dump)
1. Now, close the file (file-handle `counterfile`)
        (So that the file is closed anyways)
1. Increment the variable `count` (+1)
1. Open the file again in `'rb+'` mode
1. Dump `count` in it
1. Close the file handle
1. Finally, print the variable `count`