#!/usr/bin/env ruby
#extract sub-groups from logfile

#get commandline argument
cmdstr = ARGV[0]

#create pattern for extraction
pattern = /(from:(\w+|\+\d+).*to:(\+?\d+).*flags:(-\d.\d.-\d:\d:-\d))/

#Extract captured sub-groups
matched = pattern.match(cmdstr)

#print out matches
puts "#{matched[2]},#{matched[3]},#{matched[4]}"
