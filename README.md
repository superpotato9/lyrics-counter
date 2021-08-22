# lyrics-counter
counts the occurrences of words in song lyrics and/or can graph on a pi chart 
use 
<p> </p>
<b><i>from counter import music_sorter
  
  print(music_sorter("never gonna give you up"))</i>
  <p> </p>
  this will print the occurrences of each word as a dict formatted as {word: occur}
  or if you want it to auto create a pie chart for you do 
  <p> </p>
  <b><i> from counter import graphing<i>
    <p> </p>
    and either do 
    <b><i>graphing() </i> if you want it to prompt you in the terminal what the values are or
      <b><i> graphing('song name', how many words to show as an int)</i>
