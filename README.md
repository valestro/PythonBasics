# PythonBasics
<hr>
<h1>0_builtInPrintFunction.py</h1>
<h4><i>PRELUDE, THE print FUNCTION</i></h4>
<p>The keyword <b>print</b> is a Python <a href="https://docs.python.org/3/library/functions.html">built-in</a> function.
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

[![0_The built-in Python Keyword Print](https://github.com/valestro/PythonBasics/blob/master/pythonBasicsAllImagesGH/0_ThePythonFunctionPrint.gif?raw=true)](https://www.youtube.com/watch?v=sl3hquEpDGk&feature=youtu.be)

<hr>
<h1>1_Strings and the Backslash.py</h1>
<p>In computer programming, a <i><b>string</b></i> is zero or more characters written inside single or double quotes. 
The characters are commonly letters of the alphabet strung together into an artist's name, a quote, or a file path.
Examples:
</p>
<pre class="prettyprint lang-py prettyprinted"><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Johnny Cage'</span><span class="pln">  </span><span class="com"># Single quotes</span></pre><p>or</p>
<pre class="prettyprint lang-py prettyprinted"><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Johnny Cage"</span><span class="pln">  </span><span class="com"># Double quotes</span></pre><p>
</p>
<p>There are specific times you're going to use one over the other.
For example,  if a sentence uses single quotes surround it with double quotes.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Johnny Cage's red tinted glasses."</span></pre><p>If a sentence uses double quotes place it inside single quotes.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="str">'And then he said, "Put the alphabet in Math."'</span></pre><p>
</p>
<p>What if your sentence has double quotes and single quotes in it? How would Python know where you want to start and stop your string?</p>
<pre class="prettyprint lang-py prettyprinted"><span class="pun">>>></span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="str">"And then he said, "</span><span class="typ">Put</span><span class="pln"> the alphabet </span><span class="kwd">in</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="str">""</span>
<span class="pln">  </span><span class="typ">File</span><span class="pln"> </span><span class="str">"</span><stdin><span class="str">"</span><span class="pun">,</span><span class="pln"> line </span><span class="lit">1</span>
<span class="pln">    x </span><span class="pun">=</span><span class="pln"> </span><span class="str">"And then he said, "</span><span class="typ">Put</span><span class="pln"> the alphabet </span><span class="kwd">in</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="str">""</span>
<span class="pln">                              </span><span class="pun">^</span>
<span class="typ">SyntaxError</span><span class="pun">:</span><span class="pln"> invalid syntax</span></stdin></pre>
<p>One way to use nested double quotes is by using a backslash before the double quotes.</p>
<pre class="prettyprint lang-py>\</pre> 
<p>to make the inner double quotes into a <i>string</i> data type.
Use the backslash symbol to turn special characters, such as quotes,  into string characters. </p>
<pre class= prettyprinted" prettyprint="" lang-py"=""><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="str">"And then he said, \"Put the alphabet in Math.\""</span></pre>
<p>Whenever you use backslash and something after it, it means something special. 
</p>
<p>The backslash followed by a double quote means treat it as a string, not the start or stop of a string.</p>
<p>
</p>
<p>Another example: backslash followed by an n means go to a new line.</p>
<pre class="prettyprint lang-py>\</pre> 
<p>to make the inner double quotes into a <i>string</i> data type.
Use the backslash symbol to turn special characters, such as quotes,  into string characters. </p>
<pre class= prettyprinted" prettyprint="" lang-py"="" style="line-height: 1.42857;"><span class="pln">myFilePath </span><span class="pun">=</span><span class="pln"> </span><span class="str">"home\Desktop\niceImages"</span></pre>
<p>The above with the <span style="color: rgb(255, 160, 160); font-family: Menlo, Monaco, Consolas, " courier="" new",="" monospace;="" font-size:="" 13px;"="">\n </span>in the word niceImages is read as a new line and prints out
</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;">home/Desktop
<stdin>iceimages</stdin></pre><p>
</p>
<p>To tell python that <span style="color: rgb(255, 160, 160); font-family: Menlo, Monaco, Consolas, " courier="" new",="" monospace;="" font-size:="" 13px;"="">\n </span>should not be read as a new line, type the letter <b><i>r </i></b>before the string .</p>
<pre class="prettyprint lang-py>\</pre> 
<p>to make the inner double quotes into a <i>string</i> data type.
Use the backslash symbol to turn special characters, such as quotes,  into string characters. </p>
<pre class= prettyprinted" prettyprint="" lang-py"="" style="line-height: 1.42857;"><span class="pln">myFilePath </span><span class="pun">=</span><span class="pln"> r</span><span class="str">"home\Desktop\niceImages"</span></pre>
<p>This means print out the string in raw format, ignore all special symbols and just print it out as is. This one is useful when working with file paths.</p>
<h4>SUMMARY</h4>
<p>Use single or double quotes for strings.  Don't use quotes for numbers.</p>
<p>Backslash followed by anything has a special meaning.</p>
<p>Extra examples:</p>
<p>Can add strings together and multiply with numbers.</p>
<pre style="background-color:#2b2b2b;color:#a9b7c6;font-family:'DejaVu Sans Mono';font-size:8.3pt;">x= <span style="color:#6a8759;">"Johny"
</span>y = <span style="color:#6a8759;">"Cage"
</span><span style="color:#8888c6;">print</span>(x+y)
>>> JohnyCage
<span style="color:#8888c6;">print</span>(x*<span style="color:#6897bb;">5</span>)
>>> JohnyJohnyJohnyJohnyJohny</pre>

[![1_Strings and the Backslash](https://github.com/valestro/PythonBasics/blob/master/pythonBasicsAllImagesGH/1_stringsAndBackslash.gif?raw=true)](https://www.youtube.com/watch?v=SsWGY_zbOi8)

<hr>
<p><i>Lesson: Accessing individual characters from a string.</i></p>
<p><i>Prelude: Variables.</i></p>
<p>A <span style="font-weight: 700;">variable</span> in Python is a container <a href="https://www.tutorialspoint.com/python/python_variable_types.htm">(a reserved memory location)</a> to store values such as integers or strings.</p>
<p>To create a variable with the name <i>"</i><i>user" </i>which stores a string of capital letters, type "user" followed by the "equal sign" and lastly the string.</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="pln">user </span><span class="pun">=</span><span class="pln"> </span><span class="str">'ABCDEFGH'</span></pre><p>
</p>
<p>An important note before manipulating strings is that people usually start counting from one, for example 1, 2, 3 and so on. However computers start counting from zero, 0, 1, 2 and so on.</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="pln">user </span><span class="pun">=</span><span class="pln"> </span><span class="str">'ABCDEFGH'</span>
<span class="pln">      </span><span class="com"># 01</span><span style="font-weight: 700;"><span class="com">2345</span></span><span class="com">67</span></pre><p>To access an individual character from a variable that is holding a string, use the variable's name followed by brackets.</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="pln">user</span><span class="pun">[<font color="#cd5c5c">y</font></span><span class="pun">]</span><span class="pln">  </span><span class="com"># y can be any number from 0 to 7 since user has 8 characters and cpu starts counting at 0</span></pre><p>Inside the brackets write the position of the character you want to get, remembering that computers start counting at zero.
For example, to access the first character "A" of the string  type zero inside the brackets.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="kwd">print</span><span class="pun">(</span><span class="pln">user</span><span class="pun">[</span><span class="lit">0</span><span class="pun">])</span><span class="pln">  </span><span class="com"># A</span></pre> 
<p>Typing "1" inside the bracket prints out B.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="kwd">print</span><span class="pun">(</span><span class="pln">user</span><span class="pun">[</span><span class="lit">1</span><span class="pun">])</span><span class="pln">  </span><span class="com"># B</span></pre> 
<p>Another thing you can do is slice out a section of the string.
You write two numbers in between a colon. The first number is where to start and second where to end<b> </b><i><b>minus one</b> </i>(watch out for this).</p>
<pre class="prettyprint lang-py prettyprinted"><span class="kwd">print</span><span class="pun">(</span><span class="pln">user</span><span class="pun">[</span><span class="lit">2</span><span class="pun">:</span><span class="lit">6</span><span class="pun">])</span><span class="pln">  </span><span class="com"># CDEF</span></pre> 
<p>Notice that the second number, 6, refers to the letter G but we only got the letter up to F, that's how it works when slicing a string using the colon.</p>
<p><i>Omitting numbers</i>
When using the colon to slice a string, if you don't include the beginning Python assumes that you want to start from the very beginning. </p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="kwd">print<span class="pun" style="font-weight: normal;">(</span><span class="pln" style="font-weight: normal;">user</span><span class="pun" style="font-weight: normal;">[:</span><span class="lit" style="font-weight: normal;">3</span><span class="pun" style="font-weight: normal;">])</span><span class="pln" style="font-weight: normal;">  </span><span class="com" style="font-weight: normal;"># ABC</span></span></pre><p> Omitting the stopping point will go all the way to the end.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="kwd">print</span><span class="com"><span class="pun">(</span><span class="pln">user</span><span class="pun">[</span><span class="lit">2</span><span class="pun">:])</span><span class="pln">  </span><span class="com"># CDEFGH</span></span>
</pre> 
<p>Omitting both the start and stop position selects all the <i>positions</i>.</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="kwd">print</span><span class="pun">(</span><span class="pln">user</span><span class="pun">[:])</span><span class="pln">   </span><span class="com"># ABCDEFGH</span></pre><p><i><sub>For more on slicing strings read the below.</sub></i>
<a href="https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python" style="background-color: rgb(0, 0, 0);">Substring a string.</a>
<a href="https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation" style="background-color: rgb(0, 0, 0);">Understanding Python's slice notation.</a>
</p>
<p>
</p>
<p>Finally, lets expand our knowledge of <i>functions</i> (since they are fundamental when writing actual programs). We have seen that Python's <i>print</i>  function takes anything inside the parentheses, an input aka the <i>argument</i>, and displays it on the terminal window. 
</p>
<p>Another Python built-in function is the length function, len.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="pln">len</span><span class="pun">()</span></pre>
<p>It takes a string as an input, aka an argument , calculates how many characters it contains, and returns a number. This whole thing can then be passed as an argument to the print function.</p>
<pre class="prettyprint lang-py prettyprinted"><span class="kwd">print</span><span class="pun">(</span><span class="pln">len</span><span class="pun">(</span><span class="pln">user</span><span class="pun">))</span><span class="pln">  </span><span class="com"># 8</span></pre>

<hr>
