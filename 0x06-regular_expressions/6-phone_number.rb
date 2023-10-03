#!/usr/bin/env ruby
#Matches excactly 10 numbers

puts ARGV[0].scan(/^\d{10}$/).join
