#!/usr/bun/ruby
require "thepiratebay"; # https://github.com/emnl/thepiratebay

# NOTES
	# This script will never stop, so it must be manually stopped when it has gone past the most recent torrent available
	# This script could be running for a number of days before it has collected data about every torrent
	# "...: Error" usually suggests the torrent no longer exists

threads = [];
i = 3211593; # 3211594 is the earliest torrent. Set this to (torrent to start on - 1)
j = 0;


until j === 200 # If the script crashes, try reducing the number of threads created
	threads[j] = Thread.new() {
		while 1
			i = i + 1;
			Thread.current["todo"] = i + 0; # This is done because i will be changed by other threads between torrent = ...; and output.write(...);
			
			begin
				torrent = ThePirateBay::Torrent.find(Thread.current["todo"]);
				
				output = File.open(Thread.current.to_s + ".txt", "a+");
			
				output.write(Thread.current["todo"].to_s + ": ");
				output.write(/(?<=\()[0-9]+/.match(torrent[:size]));
				output.write("\n");
				
				output.close;
			rescue
				output = File.open(Thread.current.to_s + ".txt", "a+");
				
				output.write(Thread.current["todo"].to_s + ": Error\n");
			
				output.close;
			end
		end
	}
	
	j = j + 1;
end

threads.each { |t|
	t.join;
}