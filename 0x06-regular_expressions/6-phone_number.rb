#!/usr/bin/env ruby
# Ruby script that matches only 10 digits phone number
puts ARGV[0].scan(/^\d{10}$/).join