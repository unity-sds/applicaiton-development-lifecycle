# Algorithm Development Timeline

## Initial Script

The original script is very simple. It simply takes a file we've dowloaded and runs a trivial process on it, and ends up in a resulting file. This processing is where you'd extend the script to do soemthing more impressive or useful. 

There are two paths many users take at this stage- 

1. Some users will download all of the data they need to process locally (taking minutes to days depending on how much data is needed). This usually means that directories and how the user has stored data locally become intertwined within the code itself (e.g. loop ove my 'data' directory). We see this all the time in mission processing where all the old or incoming data are stored on a shared disk and is references explicitly- e.g. /data/{day-of-year}/my-data.nc. While this can work and make things simple, it doesn't make the processing portable or easily shareable without access to the underlying data store.
2. Other users will add the actual download of data into their code. This is helpful for portability, as it can "get" the data from wherever it is persisted (e.g. an archive). But what if the fiels are large? are you going to download that data each time you want to run the process? Or do you add some idea of caching the downloader? Now you're focusing on data management and not your algorithm- this is important to be sure, but might not be the strong suit of all algorithm developers.

After data is ready to be accessed, we simply open it, do soemthing with it, and now write some output to a data location. This data is "local" to wherever the script ran, and isn't easily shareable with other users. Users could write this to some shared file system or upload it to some shared area where others have access to it, if that's needed at all. 

Our script also does "bulk" processing, where it's doing the same thing multiple times. This logic of iteration is embedded in the code itself (e.g. for file in filenames..) which is pretty commong to intertwine the execumtion management with the processing of the data file itself. Especially with a case as trivial as this. As the processing gets more complicated, we might separate functionality into separate scripts, write intermediate files as a 'checkpoint' or a way of saving time as we iterate on the processing.


## Conversion to Notebook

1. TBD
2.    

## Dependencies



## Packaging