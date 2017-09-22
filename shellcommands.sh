#!/bin/sh

a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a = `expr $a + 1`
done ## Here is a simple example that uses the until loop to display the numbers zero to nine, 

##Grep searches the named input FILEs, By default, grep prints the matching lines. 
$ egrep -w 'word1|word2' /path/to/file ##Use grep to search 2 different words

##AWK is a powerful method for processing or analyzing text files—in particular, data files that are organized by lines (rows) and columns.
awk '{ print $5 }' table1.txt > output1.txt  ##This statement takes the element of the 5th column of each line and writes it as a line in the output file "output.txt".

# SED A stream editor is used to perform basic text transformations on an input stream
sed -n '/\([a-z][a-z]*\) \1/p' ## an example about detect duplicate words.

#head
head -n 4 foo.txt  # show the first 4 lines 
tail -n3 foo.txt  # show the last 3 lines

#this is an example about how to use both at the same time
tail -n+10 foo.txt  # start from the 10th line til the last
head -n-10 foo.txt  # print all, except the last 10 lines 

##Loops
##for loops iterate through a set of values until the list is exhausted:

#!/bin/sh
for i in hello 1 * 2 goodbye 
do
  echo "Looping ... i is set to $i"
done 
/*
"Looping ... i is set to hello
Looping ... i is set to 1
Looping ... i is set to anaconda3
Looping ... i is set to como-usar-os-comandos-eopkg.txt
Looping ... i is set to Descargas
Looping ... i is set to Documentos
Looping ... i is set to eclipse-workspace
Looping ... i is set to Escritorio
Looping ... i is set to Imágenes
Looping ... i is set to Java1
Looping ... i is set to jdk-8u144-linux-x64
Looping ... i is set to jdk-8u144-linux-x64.tar.gz
Looping ... i is set to Música
Looping ... i is set to pkg-list
Looping ... i is set to Plantillas
Looping ... i is set to Público
Looping ... i is set to PycharmProjects
Looping ... i is set to Vídeos
Looping ... i is set to 2
Looping ... i is set to goodbye" ##This is what it show de loop for.


#!/bin/sh
INPUT_STRING=hello
while [ "$INPUT_STRING" != "bye" ]
do
  echo "Please type something in (bye to quit)"
  read INPUT_STRING
  echo "You typed: $INPUT_STRING"
done
##What happens here, is that the echo and read statements will run indefinitely until you type "bye" when prompted. 

##Loop while and case
#!/bin/sh
while read f
do
  case $f in
	hello)		echo English	;;
	howdy)		echo American	;;
	gday)		echo Australian	;;
	bonjour)	echo French	;;
	"guten tag")	echo German	;;
	*)		echo Unknown Language: $f
		;;
   esac
done < myfile

## and if we want to know which number is even or odd
echo -n "Enter numnber : "
read n
 
rem=$(( $n % 2 ))
 
if [ $rem -eq 0 ]
then
  echo "$n is even number"
else
  echo "$n is odd number"
fi ##this read a number and find whether the number is odd or even

##cd - Change current directory

cd                     # go to home directory
cd ~/papers            # go to /home/user/papers
cd ~fred               # go to /home/fred

##cp - Copy file(s)

cp file1 file2                      # copy file1 to file2
cp file1 directory                  # copy file1 into directory
cp file1 file2 file3 ... directory  # copy files into directory

##file - Tells you what sort of file it is

> file temp_70.jpg 
temp_70.jpg: JPEG image data, JFIF standard 1.01,
resolution (DPI), 72 x 72


##kill - Kill, pause or continue a process. Can also be used for killing daemons.

> ps -u jss
...
 666  pts/1        06:06:06  badprocess 
> kill 666        # this sends a ``nice'' kill to the
                  # process. If that doesn't work do
> kill -KILL 666   # (or equivalently)
> kill -9 666     # which should really kill it!


##ls - Show lists of files or information on the files

ls file     # does the file exist?
ls -l file  # show information about the file
ls *.txt    # show all files ending in .txt
ls -lt      # show information about all files in date order

##man - Get instructions for a particular Unix command or a bit of Unix. Use space to get next page and q to exit.

man man      # get help on man
man grep     # get help on grep

##ps - List processes on system

> ps -u jss          # list jss's processes
  934 pts/0    00:00:00 bash
^^^^^ ^^^^^    ^^^^^^^^ ^^^^^^^
PID   output   CPU time name
> ps -f      # list processes started here in full format

##pwd - Show current working directory

> pwd
/home/jss/writing/lecture

##rm - Delete (remove) files

rm file1     # delete a file (use -i to ask whether sure)
rm -r dir1   # delete a directory and everything in it (CARE!)


