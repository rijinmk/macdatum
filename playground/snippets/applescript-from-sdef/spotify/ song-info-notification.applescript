-- This is a script to use with Spotify which give information of the song you listening to.

-- Check if Spotify is open
if application "Spotify" is running then
	-- If Spotify is open
	tell application "Spotify"
		-- Keep checking for next song to start
		repeat while (player state) is not stopped
			-- Check if the song is playing
			if (player state) is playing then
				-- If the player position is 0 i.e start of the song
				if ((round (get player position) rounding down) = 0) then
					-- Reduce Spotify volume by 25%
					set vol to (sound volume) * 0.25
					set (sound volume) to ((sound volume) - vol)
					-- Give information about the song i.e name of the song and artist
					say "You are listening to, " & (get (name of current track) as string) & " by " & (get (artist of current track) as string)
					-- Increase Spotify volume by 25%
					set (sound volume) to ((sound volume) + vol)
				end if
			end if
		end repeat
	end tell
else
	return "Spotify"
end if
return