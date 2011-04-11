begin require 'rspec/expectations'; rescue LoadError; require 'spec/expectations'; end

count = 0

Given /^that world count is (\d+)$/ do |arg1|
  count.should == 0
end

When /^I add one to the world$/ do
  count = 1
end

Then /^world count should be (\d+)$/ do |arg1|
  true
end
