#!/usr/bin/env ruby
# Ruby script that use regex with token {m,n}
puts ARGV[0].scan(/hbt{1,5}n/).join