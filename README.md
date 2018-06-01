# PythonBasics
<h2>PRELUDE, THE print FUNCTION</h2>
<p>The keyword <span style="color:orange">print</span> is a Python <a href="https://docs.python.org/3/library/functions.html">built-in</a> function.
<i>A function</i>  takes an input, placed inside parentheses, and returns an output.
The <i>function</i> <span style="color:orange">print</span> is simple,<i> it takes anything inside of the parentheses and displays it on the terminal screen.</i>
For example, to show the output of the input calculation
</p>
<pre class="prettyprint lang-py prettyprinted"><span class="lit">5</span><span class="pun">+</span><span class="lit">8</span></pre><p>you would type</p>
<pre class="prettyprint lang-py prettyprinted"><span class="kwd">print</span><span class="pun">(</span><span class="lit">5</span><span class="pun">+</span><span class="lit">8</span><span class="pun">)</span></pre>
<p>in a python console, hit enter, and the output will be shown in the next line as 13.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="pun">>>></span><span class="pln"> </span><span class="kwd">print</span><span class="pun">(</span><span class="lit">5</span><span class="pun">+</span><span class="lit">8</span><span class="pun">)</span>
<span class="lit">13</span>
<span class="pun">>>></span><span class="pln"> </span><span class="kwd">print</span><span class="pun">(</span><span class="str">"hello"</span><span class="pun">)</span>
<span class="pln">hello</span></pre>
<p>To display words using the print function, the words must be surrounded by single or double quotes.</p>
<p><i>Below is from Sentdex YouTube video. See Link1 below.</i>
"The print function in Python is a function that outputs to your console window whatever you say you want to print out. At first blush, it might appear that the print function is rather useless for programming, but it is actually one of the most widely used functions in all of python. The reason for this is that it makes for a great debugging tool. If something isn't acting right, you can use the print function to print out what is happening in the program. Many times, you expect a certain variable to be one thing, but you cannot see what the program sees. If you print out the variable, you might see that what you thought was, was not."</p>
<p style="color:lightblue;font-size:18px">Next Lesson</p>
<p>Next up, strings, what are they? Strings are letters or numbers inside single or double quotes. Strings are a type of data. Another type of data are integers (aka whole numbers like 5 and 8 and not like 2.71 a decimal.<a href="https://www.w3schools.com/js/js_numbers.asp">Not in JS</a>).
</p>
<p>SUMMARY</p>
>>> print(5+8)
13
>>> print 5+8  # SyntaxError: Missing parentheses in call to 'print'. Works in Python 2.
SyntaxError
>>> print('I am a sentence.')
I am a sentence.
>>> print("I am also a sentence, aka a string.")  # Note the double quotes
I am also a sentence, aka a string.
