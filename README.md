<h1>python-test</h1>
<h3>python test, question and answers</h3>
</br>Please Read question try to resolve one by one, after each try and done, download my answers and check with your answers.
</br><i>let me know how to resolve the questions</i>
</br>
</br>
</br>
<h2>1- Capital indexes</h2>
Write a function named <code>capital_indexes</code>. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling <code>capital_indexes("HeLlO")</code> should return the list <code>[0, 2, 4]</code>.


<h2>2- Middle letter</h2>
Write a function named <code>mid</code> that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, <code>mid("abc")</code> should return <code>"b"</code> and <code>mid("aaaa")</code> should return <code>""</code>.

<h2>3- Online status</h2>
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:
<pre>
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
</pre>
In this case, the number of people online is <code>2</code>.

Write a function named <code>online_count</code> that takes one parameter. The parameter is a dictionary that maps from strings of names to the string <code>"online"</code> or <code>"offline"</code>, as seen above.

Your function should return the number of people who are online.

<h2>4- Randomness</h2>

Define a function, <code>random_number</code>, that takes no parameters. The function must generate a random integer between <code>1</code> and <code>100</code>, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling <code>random_number()</code> some times might first return <code>42</code>, then <code>63</code>, then <code>1</code>.


<h2>5- Type check</h2>
Write a function named <code>only_ints</code> that takes two parameters. Your function should return <code>True</code> if both parameters are integers, and <code>False</code> otherwise.

For example, <code>calling only_ints(1, 2)</code> should return <code>True</code>, while calling <code>only_ints("a", 1)</code> should return <code>False</code>.

<h2>6- Double letters</h2>
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string <code>"hello"</code> has l twice in a row, while the string <code>"nono"</code> does not have two identical letters in a row.

Define a function named <code>double_letters</code> that takes a single parameter. The parameter is a string. Your function must return <code>True</code> if there are two identical letters in a row in the string, and <code>False</code> otherwise.

<h2>7- Adding and removing dots</h2>
Write a function named <code>add_dots</code> that takes a string and adds <code>"."</code> in between each letter. For example, calling <code>add_dots("test")</code> should return the string <code>"t.e.s.t"</code>.

Then, below the <code>add_dots</code> function, write another function named <code>remove_dots</code> that removes all dots from a string. For example, calling <code>remove_dots("t.e.s.t")</code> should return <code>"test"</code>.

If both functions are correct, calling <code>remove_dots(add_dots(string))</code> should return back the original string for any string.

(You may assume that the input to <code>add_dots</code> does not itself contain any dots.)


<h2>8- Counting syllables</h2>
Define a function named <code>count</code> that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

<pro>"ho-tel"
    "cat"
    "met-a-phor"
    "ter-min-a-tor"
    Your function should count the number of syllables and return it.
</pro>

For example, the call <code>count("ho-tel")</code> should return <code>2</code>.

<h2>9- Anagrams</h2>
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named <code>is_anagram</code> that takes two strings as its parameters. Your function should return <code>True</code> if the strings are anagrams, and <code>False</code> otherwise.

For example, the call <code>is_anagram("typhoon", "opython")</code> should return True while the call <code>is_anagram("Alice", "Bob")</code> should return <code>False</code>.

<h2>10- Flatten a list</h2>
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function <code>flatten</code>. It should take a single parameter and return a list.

For example, calling:

<code>flatten([[1, 2], [3, 4]])</code>

Should return the list:

<code>[1, 2, 3, 4]</code>




___________________________________________________________________________________________________
<br><h6>Source is pythonprinciples</h6></br>
