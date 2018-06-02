# PythonBasics
<hr>
<h2>0_builtInPrintFunction.py</h2>
<h3><i>PRELUDE, THE print FUNCTION</i></h3>
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

[![The built-in Python Keyword Print](https://github.com/valestro/PythonBasics/blob/master/pythonBasicsAllImagesGH/theBuiltPythonKeywordPrint.mp4gifFromOgv.gif?raw=true)](https://www.youtube.com/watch?v=sl3hquEpDGk&feature=youtu.be)

<hr>

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

<hr>
