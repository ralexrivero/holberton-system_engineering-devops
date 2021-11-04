#!/usr/bin/env ruby
# Ruby script that acepts one argument and use {m,n} token
puts ARGV[0].scan(/h(b|t){1,2}n/).join