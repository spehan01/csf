# Name: Hannah Spencer
# Evergreen Login: spehan01
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
a_count = 0
t_count = 0
g_count = 0
c_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':      
        # increment the count of gc
        gc_count = gc_count + 1
    elif bp == 'A' or bp == 'T':
        at_count = at_count + 1
    if bp == 'A':
        a_count = a_count + 1
    elif bp == 'T':
        t_count = t_count + 1
    elif bp == 'G':
        g_count = g_count + 1
    elif bp == 'C':
        c_count = c_count +1   
              
sum_count = a_count + t_count + g_count + c_count
ratio = float(at_count) / float(gc_count)

# divide the gc_count by the total_count
gc_content = float(gc_count) / sum_count
at_content = float(at_count) / sum_count

if gc_content >= float(0.6):
    gc_class = 'High GC content'
elif gc_content <= float(0.4):
    gc_class = 'Low GC content'
else:
    gc_class = 'Moderate GC content'
print gc_class

# Print the answer
print 'GC-content:', gc_content
print 'AT_content:', at_content
print 'A_count:', a_count
print 'T_count:', t_count
print 'G_count:', g_count
print 'C_count:', c_count
print 'Sum_count:', sum_count
print 'Total_count:', total_count
print 'seg length:', len(seq)
print 'AT/GC Ratio:', ratio
print 'GC Classification:', gc_class