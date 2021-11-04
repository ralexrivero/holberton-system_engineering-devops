#!/usr/bin/env ruby
# Ruby script that use regex with {m,n} token
puts ARGV[0].scan(/hbt{,5}n/).join