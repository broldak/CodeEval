class Stack
    attr_accessor :list

	def initialize
		@list = []
	end

	def pop
		x = @list[-1]
		@list = @list[0..-2]
		x
	end

	def push x
		@list << x
	end
end

File.open(ARGV[0]).each_line do |line|
  ints = line.split(' ').map(&:to_i)

  stack = Stack.new
  ints.each do |i|
    stack.push i
  end

  items = []
  ints.each do
    items << stack.pop
    stack.pop
  end

  puts items.join(' ')
end
